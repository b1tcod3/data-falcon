//! Aquí usamos thiserror para definir errores específicos que nuestra lógica interna debe reconocer.

use thiserror::Error;

#[derive(Error, Debug)]
pub enum AppError {
    #[error("Archivo no encontrado: {0}")]
    FileNotFound(String),

    #[error("Error de validación: {0}")]
    ValidationError(String),

    #[error("Error de red")]
    NetworkError(#[from] reqwest::Error),
}
