//! Aquí es donde anyhow brilla, permitiéndonos mezclar diferentes tipos de errores.

use crate::errors::AppError;
use crate::models::{Config, User};
use anyhow::{anyhow, bail, Context, Result};
use std::fs;
use std::path::Path;

pub struct DataProcessor {
    pub config: Config,
}

impl DataProcessor {
    pub fn new(config_path: &str) -> Result<Self> {
        // .with_context es "lazy": solo evalúa el closure si hay error
        let config_str = fs::read_to_string(config_path)
            .with_context(|| format!("No se pudo leer el archivo: {config_path}"))?;

        let config: Config =
            serde_json::from_str(&config_str).context("Error al parsear la configuración JSON")?;

        if config.api_key.is_empty() {
            bail!("La clave API no puede estar vacía"); // Error rápido con mensaje
        }

        if config.timeout == 0 {
            // Mezclamos un error específico de AppError dentro de anyhow
            bail!(AppError::ValidationError("Timeout debe ser > 0".into()));
        }

        Ok(DataProcessor { config })
    }

    pub fn process_user(&self, user_json: &str) -> Result<User> {
        let user: User = serde_json::from_str(user_json).context("Error en JSON de usuario")?;
        self.validate_user(&user)?;
        Ok(user)
    }

    /// Procesa un archivo con manejo de errores en cadena
    pub fn process_file(&self, file_path: &str) -> Result<Vec<User>> {
        // Verificar si el archivo existe
        if !Path::new(file_path).exists() {
            // Usando error personalizado
            return Err(AppError::FileNotFound(file_path.to_string()).into());
        }

        // Leer archivo
        let content = fs::read_to_string(file_path)
            .with_context(|| format!("Error al leer archivo {}", file_path))?;

        // Dividir en líneas y procesar
        let mut users = Vec::new();
        for (line_num, line) in content.lines().enumerate() {
            if line.trim().is_empty() {
                continue;
            }

            match self.process_user(line) {
                Ok(user) => users.push(user),
                Err(e) => {
                    // Agregar contexto sobre la línea
                    eprintln!("Advertencia: Error en línea {}: {}", line_num + 1, e);
                    // Podríamos continuar procesando o parar aquí
                }
            }
        }

        if users.is_empty() {
            bail!("No se pudo procesar ningún usuario del archivo");
        }

        Ok(users)
    }

    fn validate_user(&self, user: &User) -> Result<()> {
        if user.name.trim().is_empty() {
            bail!(AppError::ValidationError("Nombre vacío".into()));
        }
        if !user.email.contains('@') {
            bail!(AppError::ValidationError("Email inválido".into()));
        }
        Ok(())
    }

    pub async fn fetch_data(&self, url: &str) -> Result<String> {
        let client = reqwest::Client::builder()
            .timeout(std::time::Duration::from_secs(self.config.timeout as u64))
            .build()
            .context("Error al crear cliente HTTP")?;

        let response = client
            .get(url)
            .header("Authorization", format!("Bearer {}", self.config.api_key))
            .send()
            .await
            .context("Error en la solicitud HTTP")?;

        if !response.status().is_success() {
            let status = response.status();
            let text = response.text().await.unwrap_or_default();
            bail!(anyhow!("Status {}: {}", status, text));
        }

        Ok(response.text().await?)
    }
}
