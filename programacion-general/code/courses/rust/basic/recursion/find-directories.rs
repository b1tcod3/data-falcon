//! Algoritmo de búsqueda recursiva de directorios en Rust
//!
//! Este módulo contiene una implementación de búsqueda recursiva de subdirectorios,
//! similar al comando Unix `find`. El algoritmo recorre un directorio dado y busca
//! todos los subdirectorios de forma recursiva, imprimiendo la ruta de cada directorio
//! encontrado.

//use std::fs::{self, DirEntry};
use std::fs;
use std::path::Path;

/// Busca e imprime todos los subdirectorios de forma recursiva
///
/// Esta función recorre el directorio especificado y todos sus subdirectorios,
/// imprimiendo la ruta de cada directorio encontrado. Excluye los directorios
/// especiales "." (actual) y ".." (padre).
///
/// # Parámetros
/// * `directory` - Una referencia a una cadena que contiene la ruta al directorio
///   donde comenzar la búsqueda.
///
/// # Ejemplo
/// ```
/// use std::path::Path;
///
/// // Buscar directorios en el directorio actual
/// find_directories(".");
///
/// // Buscar en un directorio específico
/// find_directories("/home/usuario/documentos");
/// ```
///
/// # Complejidad
/// * Tiempo: O(n) donde n es el número total de directorios encontrados
/// * Espacio: O(d) donde d es la profundidad máxima del árbol de directorios
///   (debido a la recursión en la pila de llamadas)
///
/// # Notas
/// - La función ignora archivos que no son directorios
/// - Los directorios "." y ".." son excluidos automáticamente
/// - Imprime cada directorio encontrado en una nueva línea
pub fn find_directories(directory: &str) {
    let path = Path::new(directory);

    if let Ok(entradas) = fs::read_dir(path) {
        for entrada in entradas.flatten() {
            let ruta = entrada.path();
            let nombre = entrada.file_name();

            // Filtrar directorios especiales "." y ".."
            if let Some(nombre_str) = nombre.to_str() {
                if nombre_str == "." || nombre_str == ".." {
                    continue;
                }
            }

            // Verificar si es un directorio
            if ruta.is_dir() {
                // Imprimir la ruta del directorio
                if let Some(ruta_str) = ruta.to_str() {
                    println!("{}", ruta_str);
                }

                // Llamada recursiva para buscar en subdirectorios
                if let Some(ruta_str) = ruta.to_str() {
                    find_directories(ruta_str);
                }
            }
        }
    }
}

fn main() {
    println!("Buscando directorios en el directorio actual:");
    find_directories(".");
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;
    use std::path::PathBuf;

    #[test]
    fn test_encuentra_subdirectorios() {
        let temp_dir = PathBuf::from("/tmp/test_rust_find_directories");
        let _ = fs::remove_dir_all(&temp_dir);

        let subdir1 = temp_dir.join("subdir1");
        let subdir2 = temp_dir.join("subdir2");
        let subdir2_nested = subdir2.join("nested");

        fs::create_dir_all(&subdir1).unwrap();
        fs::create_dir_all(&subdir2_nested).unwrap();

        // La función debería encontrar los subdirectorios
        find_directories(temp_dir.to_str().unwrap());

        // Limpiar
        let _ = fs::remove_dir_all(&temp_dir);
    }

    #[test]
    fn test_directorio_vacio() {
        let temp_dir = PathBuf::from("/tmp/test_rust_find_empty");
        let _ = fs::remove_dir_all(&temp_dir);
        fs::create_dir_all(&temp_dir).unwrap();

        // No debería fallar con directorio vacío
        find_directories(temp_dir.to_str().unwrap());

        fs::remove_dir(&temp_dir).ok();
    }
}
