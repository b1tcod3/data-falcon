// Ejercicio secuencial: conversiones de un gimnasio (version PSeInt)
//
// Una persona tiene un peso inicial. Primero el peso disminuye un 28.5% y
// luego aumenta un 5% con respecto al peso resultante. El objetivo es
// expresar el peso final en kilogramos, miligramos, libras, onzas y
// quintales.
//   1 kg = 1,000,000 mg ; 1 kg = 2.2205 lb ; 1 lb = 16 onzas ;
//   1 quintal = 100 kg

Algoritmo GimnasioConversiones
    Definir peso_inicial Como Real
    Definir peso, peso_tras_bajar Como Real
    Definir miligramos, libras, onzas, quintales Como Real
    Definir disminucion, aumento Como Real
    Definir mg_por_kg, lb_por_kg, onzas_por_lb, kg_por_quintal Como Real

    disminucion <- 0.285
    aumento <- 0.05
    mg_por_kg <- 1000000
    lb_por_kg <- 2.2205
    onzas_por_lb <- 16
    kg_por_quintal <- 100

    Escribir "Peso inicial (kg):"
    Leer peso_inicial

    peso_tras_bajar <- peso_inicial * (1 - disminucion)
    peso <- peso_tras_bajar * (1 + aumento)

    miligramos <- peso * mg_por_kg
    libras <- peso * lb_por_kg
    onzas <- libras * onzas_por_lb
    quintales <- peso / kg_por_quintal

    Escribir ""
    Escribir "=== Peso final y sus equivalentes ==="
    Escribir "Kilogramos: ", peso, " kg"
    Escribir "Miligramos: ", miligramos, " mg"
    Escribir "Libras: ", libras, " lb"
    Escribir "Onzas: ", onzas, " onzas"
    Escribir "Quintales: ", quintales, " quintales"
FinAlgoritmo
