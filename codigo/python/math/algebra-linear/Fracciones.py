import math

class Fraccion:
    def __init__(self, numerador, denominador=1):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero")
        
        if denominador < 0:
            numerador = -numerador
            denominador = abs(denominador)
        
        gcd = math.gcd(abs(numerador), denominador)
        self.numerador = numerador // gcd
        self.denominador = denominador // gcd
    
    def __add__(self, other):
        other = self._convert_to_fraccion(other)
        nuevo_numerador = self.numerador * other.denominador + other.numerador * self.denominador
        nuevo_denominador = self.denominador * other.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __sub__(self, other):
        other = self._convert_to_fraccion(other)
        nuevo_numerador = self.numerador * other.denominador - other.numerador * self.denominador
        nuevo_denominador = self.denominador * other.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __mul__(self, other):
        other = self._convert_to_fraccion(other)
        nuevo_numerador = self.numerador * other.numerador
        nuevo_denominador = self.denominador * other.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __truediv__(self, other):
        other = self._convert_to_fraccion(other)
        nuevo_numerador = self.numerador * other.denominador
        nuevo_denominador = self.denominador * other.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __floordiv__(self, other):
        other = self._convert_to_fraccion(other)
        nuevo_numerador = self.numerador // other.numerador
        nuevo_denominador = self.denominador // other.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    # Operadores de comparación
    def __eq__(self, other):
        other = self._convert_to_fraccion(other)
        return (self.numerador * other.denominador) == (other.numerador * self.denominador)
    
    def __lt__(self, other):
        other = self._convert_to_fraccion(other)
        return (self.numerador * other.denominador) < (other.numerador * self.denominador)
    
    def __le__(self,other):
        return self < other or self == other
    
    def __gt__(self,other):
        return not self <= other
    
    def __ge__(self,other):
        return not self < other
    
    def __ne__(self,other):
        return not self == other
    
    def __repr__(self):
        return f"Fraccion({self.numerador}, {self.denominador})"
    
    def to_float(self):
        return self.numerador / self.denominador
    
    def to_decimal(self, precision=4):
        return round(self.numerador / self.denominador, precision)
    
    def _convert_to_fraccion(self, value):
        if isinstance(value, int):
            return Fraccion(value)
        elif isinstance(value, float):
            return self._float_to_fraction(value)
        elif isinstance(value, Fraccion):
            return value
        else:
            raise TypeError("No se puede convertir a fraccion")
    
    def __str__(self):
        if self.denominador == 1:
            return str(self.numerador)
        return f"{self.numerador}/{self.denominador}"
    
    def _float_to_fraction(self, value, tolerance=1e-9, max_denominator=100000000):
        """
        Convierte un decimal en fraccion usando precisión controlada
        """
        
        if value == 0.0:
            return Fraccion(0, 1)
        
        #manejar signo
        signo = 1
        if value < 0:
            signo = -1
            value = -value
        
        # separar parte entera y decimal
        parte_entera = int(value)
        decimal = value - parte_entera
        
        if decimal < tolerance:
            return Fraccion(signo * parte_entera, 1)
        
        # inicializar mejores valores
        mejor_numerator = 0
        mejor_denominator = 1
        mejor_error = abs(value)
        
        # buscar fraccion
        for denominador in range(1, max_denominator + 1):
            numerador = round(decimal * denominador)
            
            actual_valor = parte_entera + numerador / denominador
            actual_error = abs(value - actual_valor)
            
            if actual_error < mejor_error:
                mejor_numerator = numerador
                mejor_denominator = denominador
                mejor_error = actual_error

                if mejor_error < tolerance:
                    break
        
        numerador = signo * (parte_entera * mejor_denominator + mejor_numerator)
        
        return Fraccion(numerador, mejor_denominator)
        
if __name__ == "__main__":
    f1 = Fraccion(1, 2)
    f2 = Fraccion(1, 3)
    f3 = Fraccion(1, 4)
    print(f1*f2+f3)