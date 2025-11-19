import secrets
import time
import os
import sys

def tirar_dado():
    # Combinación de múltiples fuentes de entropía
    entropy = secrets.token_bytes(16) + bytes(str(time.perf_counter_ns()), 'utf-8')
    entropy += os.urandom(8) + bytes(str(os.getpid()), 'utf-8')
    
    # Generación robusta usando SystemRandom
    rand = secrets.SystemRandom()
    rand.seed(entropy)
    
    # Doble generación para mayor aleatoriedad
    resultado = rand.randint(1, 100)
    resultado = (resultado + rand.randint(1, 100)) % 100 + 1
    
    return resultado

if __name__ == "__main__":
    print("🎲 Tirando dado de 100 caras...")
    print(f"⭐ Resultado: {tirar_dado()}")