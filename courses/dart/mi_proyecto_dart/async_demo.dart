// 1. Función Asíncrona (marcada con async)
Future<String> simularDescarga(int segundos) async {
  print('Iniciando descarga (duración: $segundos segundos)...');
  
  // 2. Simulamos una espera con Future.delayed
  // Esto no bloquea el resto del programa.
  await Future.delayed(Duration(seconds: segundos));
  
  // 3. El Future se completa y devuelve el resultado
  return 'Datos descargados exitosamente en $segundos segundos.';
}

// La función main debe ser asíncrona para poder usar 'await'
void main() async {
  print('--- Inicio del Programa ---');
  
  // 4. Usamos await para esperar el resultado de simularDescarga
  try {
    String resultado = await simularDescarga(2); // Espera 2 segundos
    print(resultado);
    
    // Podemos ejecutar otra operación asíncrona
    String otroResultado = await simularDescarga(1); // Espera 1 segundo
    print(otroResultado);
  } catch (e) {
    // Si la descarga fallara, el error se capturaría aquí
    print('Error capturado: $e');
  }

  print('--- Fin del Programa (el código no bloqueado se ejecutó aquí) ---');
}
