void main() {
  // Listas (List)
  List<String> frutas = ['manzana', 'banana', 'kiwi'];
  frutas.add('naranja');
  print('Lista de frutas: $frutas');
  print('Primera fruta: ${frutas[0]}');

  // Conjuntos (Set)
  Set<int> numerosUnicos = {10, 20, 30, 20}; // El 20 duplicado se ignora
  print('Conjunto de números: $numerosUnicos');
  numerosUnicos.add(40);
  print('Tamaño del conjunto: ${numerosUnicos.length}');
  
  // Mapas (Map)
  Map<String, dynamic> usuario = {
    'nombre': 'Elena',
    'activo': true,
    'puntos': 150
  };
  usuario['email'] = 'elena@ejemplo.com'; // Añadir un nuevo par
  
  print('Datos del usuario: ${usuario['nombre']}, Puntos: ${usuario['puntos']}');
  
  // Iterar sobre un Mapa
  usuario.forEach((key, value) {
    print('$key: $value');
  });
}
