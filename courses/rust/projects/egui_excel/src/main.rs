use chrono::NaiveDate;
use eframe::egui;
use rust_xlsxwriter::*;

fn main() -> eframe::Result {
    let options = eframe::NativeOptions::default();
    eframe::run_native(
        "Formulario de Registro",
        options,
        Box::new(|_cc| Ok(Box::new(MyForm::default()))),
    )
}

struct MyForm {
    nombre: String,
    cedula: String,
    cargo: String,
    municipio_seleccionado: String,
    municipios: Vec<String>,
    fecha_nacimiento: String,
}

impl Default for MyForm {
    fn default() -> Self {
        Self {
            nombre: String::new(),
            cedula: String::new(),
            cargo: String::new(),
            municipios: vec![
                "Libertador".into(),
                "Chacao".into(),
                "Sucre".into(),
                "Baruta".into(),
            ],
            municipio_seleccionado: "Libertador".into(),
            fecha_nacimiento: "1990-01-01".into(),
        }
    }
}

impl eframe::App for MyForm {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.heading("Registro de Personal");
            ui.add_space(10.0);

            ui.horizontal(|ui| {
                ui.label("Nombre y Apellido:");
                ui.text_edit_singleline(&mut self.nombre);
            });

            ui.horizontal(|ui| {
                ui.label("Cédula:");
                ui.text_edit_singleline(&mut self.cedula);
            });

            ui.horizontal(|ui| {
                ui.label("Cargo:");
                ui.text_edit_singleline(&mut self.cargo);
            });

            ui.horizontal(|ui| {
                ui.label("Municipio:");
                egui::ComboBox::from_id_source("municipio_combo")
                    .selected_text(&self.municipio_seleccionado)
                    .show_ui(ui, |ui| {
                        for m in &self.municipios {
                            ui.selectable_value(&mut self.municipio_seleccionado, m.clone(), m);
                        }
                    });
            });

            ui.horizontal(|ui| {
                ui.label("Fecha Nacimiento (AAAA-MM-DD):");
                ui.text_edit_singleline(&mut self.fecha_nacimiento);
            });

            ui.add_space(20.0);

            if ui.button("Guardar en Excel").clicked() {
                if let Err(e) = self.guardar_en_excel() {
                    eprintln!("Error al guardar: {}", e);
                } else {
                    println!("¡Guardado exitosamente!");
                }
            }
        });
    }
}

impl MyForm {
    fn guardar_en_excel(&self) -> Result<(), XlsxError> {
        // CORRECCIÓN 1: El error dice que 'new' requiere el nombre del archivo
        let mut workbook = Workbook::new("registro_personal.xlsx");

        let worksheet = workbook.add_worksheet();

        // Creamos los formatos necesarios
        let fmt_header = Format::new().set_bold();
        let fmt_normal = Format::new(); // Formato vacío para cumplir con el requisito de 4 argumentos
        let fmt_date = Format::new().set_num_format("yyyy-mm-dd");

        // CORRECCIÓN 2: Usamos write_string pasando SIEMPRE el formato (4 argumentos)
        // Encabezados (usando fmt_header)
        worksheet.write_string(0, 0, "Nombre y Apellido", &fmt_header)?;
        worksheet.write_string(0, 1, "Cédula", &fmt_header)?;
        worksheet.write_string(0, 2, "Cargo", &fmt_header)?;
        worksheet.write_string(0, 3, "Municipio", &fmt_header)?;
        worksheet.write_string(0, 4, "Fecha de Nacimiento", &fmt_header)?;

        // Datos (usando fmt_normal porque write_string exige un formato)
        worksheet.write_string(1, 0, &self.nombre, &fmt_normal)?;
        worksheet.write_string(1, 1, &self.cedula, &fmt_normal)?;
        worksheet.write_string(1, 2, &self.cargo, &fmt_normal)?;
        worksheet.write_string(1, 3, &self.municipio_seleccionado, &fmt_normal)?;

        // Manejo de la fecha
        if let Ok(date) = NaiveDate::parse_from_str(&self.fecha_nacimiento, "%Y-%m-%d") {
            // write_date también requerirá el formato
            worksheet.write_date(1, 4, date, &fmt_date)?;
        } else {
            // Si falla la fecha, escribimos como texto con formato normal
            worksheet.write_string(1, 4, &self.fecha_nacimiento, &fmt_normal)?;
        }

        // CORRECCIÓN 3: Si 'save()' no existe, usamos 'close()' o dejamos que Rust lo cierre al final.
        // En las librerías que piden el nombre en el new(), close() es el método estándar.
        workbook.close()?;

        Ok(())
    }
}
