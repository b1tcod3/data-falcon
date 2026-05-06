//! Separamos los datos de la lógica de procesamiento.

use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct Config {
    pub api_key: String,
    pub timeout: u32,
    pub retries: u8,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct User {
    pub id: u32,
    pub name: String,
    pub email: String,
}
