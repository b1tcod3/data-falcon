fn sumar_elementos(lista: &[i32]) -> i32 {
    let mut total = 0;
    for numero in lista {
        total += numero;
    }
    total
}

fn main(){

    let corto = [1,2,3];
    let largo = [1,2,3,4,5,6,7,8,9,10];

    println!("La suma de los elementos en corto es: {}", sumar_elementos(&corto));
    println!("La suma de los elementos en largo es: {}", sumar_elementos(&largo));
}
