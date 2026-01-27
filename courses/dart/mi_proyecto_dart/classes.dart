class Persona{
    final String nombre;
    final int edad;

    String? ocupacion;
    Persona(this.nombre, this.edad);

    void saludar(){
        print('Hola mi nombre es $nombre y tengo $edad años.');

        if (ocupacion == null){
            print('Trabajo como $ocupacion.');
        }
    }        
    Persona.trabajador(this.nombre, this.edad, this.ocupacion);
}

void main(){

    var persona1 = Persona('Carla',34);
    persona1.saludar();
}
