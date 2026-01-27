fn main(){

    let temperatura_semanal = [22.5, 24.0, 19.5, 21.0, 23.5, 20.0, 18.5];
    let mut suma = 0.0;

    let umbral_calor = 30.0;

    println!("Análisis de temperaturas semanales:");

    for (i,temp) in temperatura_semanal.iter().enumerate() {
        println!("Día {}: {:.1}°C", i + 1, temp);
        suma += temp;

        if *temp > umbral_calor {
            println!("  ¡Alerta! Temperatura alta detectada.");
        }
    }

    let promedio = suma / temperatura_semanal.len() as f32;
    println!("Temperatura promedio semanal: {:.1}°C", promedio);
}
