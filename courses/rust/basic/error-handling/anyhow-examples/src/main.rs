/// ejemplos de uso de la biblioteca anyhow para manejo de errores en Rust
mod errors;
mod models;
mod processor;

use anyhow::{anyhow, Context, Result};
use processor::DataProcessor;

#[tokio::main]
async fn main() -> Result<()> {
    println!("=== Ejemplos de uso de Anyhow ===");

    // Ejemplo 1: Crear y Usar DataProcessor

    match DataProcessor::new("config.json") {
        Ok(processor) => {
            println!("DataProcessor creado exitosamente.");
            println!("Config: {:?}", processor.config);

            // ejemplo de procesamiento de usuariosº
            let user_json = r#"
            {
                "name": "Juan Perez",
                "age": 30,
                "email": "juan@eexample.com"
            }"#;

            match processor.process_user(user_json) {
                Ok(user) => println!("Usuario procesado: {:?}", user),
                Err(e) => eprintln!("Error al procesar datos: {:?}", e),
            }

            // ejemplo de archivo
            println!("\n === Ejemplo de manejo de archivos ===");
            match processor.process_file("usuarios.txt") {
                Ok(users) => {
                    println!("Usuarios procesados desde archivo:{}", users.len());
                    for user in users {
                        println!(" - {}, ({})", user.name, user.email);
                    }
                }
                Err(e) => {
                    println!("Error al procesar archivo: {:?}", e);
                    // podemos inspeccionar el error más a fondo
                    if let Some(io_err) = e.downcast_ref::<std::io::Error>() {
                        println!("Error de IO detallado: {}", io_err);
                    }
                }
            }
        }
        Err(e) => {
            eprintln!("Error al crear DataProcessor: {:?}", e);
        }
    }
    println!("\n === Ejemplos Adicionales de Anyhow ===");

    match example_error_mixing() {
        Ok(_) => println!("Ejemplos adicionales ejecutados correctamente."),
        Err(e) => eprintln!("Error en ejemplos adicionales: {:?}", e),
    }
    Ok(())
}
