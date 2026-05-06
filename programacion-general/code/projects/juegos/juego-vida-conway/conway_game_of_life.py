#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Juego de la Vida de Conway

Un autómata celular diseñado por el matemático británico John Horton Conway en 1970.

Reglas:
1. Cualquier célula viva con menos de dos vecinas vivas muere por soledad.
2. Cualquier célula viva con dos o tres vecinas vivas sobrevive a la siguiente generación.
3. Cualquier célula viva con más de tres vecinas vivas muere por sobrepoblación.
4. Cualquier célula muerta con exactamente tres vecinas vivas se convierte en una célula viva.
"""

import os
import time
import random
import numpy as np
from typing import List, Tuple, Set


class GameOfLife:
    """Clase que implementa el Juego de la Vida de Conway."""
    
    def __init__(self, rows: int = 30, cols: int = 50):
        """
        Inicializa el tablero del juego.
        
        Args:
            rows: Número de filas del tablero.
            cols: Número de columnas del tablero.
        """
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)
        self.generation = 0
        
    def clear_screen(self):
        """Limpia la pantalla de la consola."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display(self):
        """Muestra el estado actual del tablero en la consola."""
        self.clear_screen()
        print(f"Juego de la Vida de Conway - Generación: {self.generation}")
        print("-" * (self.cols + 2))
        
        for row in self.grid:
            print("|", end="")
            for cell in row:
                print("█" if cell else " ", end="")
            print("|")
        
        print("-" * (self.cols + 2))
        
    def set_cell(self, row: int, col: int, state: int = 1):
        """
        Establece el estado de una célula específica.
        
        Args:
            row: Fila de la célula.
            col: Columna de la célula.
            state: Estado de la célula (1 para viva, 0 para muerta).
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row, col] = state
            
    def toggle_cell(self, row: int, col: int):
        """
        Cambia el estado de una célula específica.
        
        Args:
            row: Fila de la célula.
            col: Columna de la célula.
        """
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row, col] = 1 - self.grid[row, col]
            
    def get_neighbors(self, row: int, col: int) -> int:
        """
        Cuenta el número de células vecinas vivas.
        
        Args:
            row: Fila de la célula central.
            col: Columna de la célula central.
            
        Returns:
            Número de células vecinas vivas.
        """
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                r, c = row + i, col + j
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    count += self.grid[r, c]
        return count
    
    def next_generation(self):
        """Calcula la siguiente generación del juego."""
        new_grid = np.zeros_like(self.grid)
        
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.get_neighbors(row, col)
                
                # Aplicar las reglas del juego
                if self.grid[row, col] == 1:  # Célula viva
                    if neighbors < 2 or neighbors > 3:  # Muere por soledad o sobrepoblación
                        new_grid[row, col] = 0
                    else:  # Sobrevive
                        new_grid[row, col] = 1
                else:  # Célula muerta
                    if neighbors == 3:  # Nace una nueva célula
                        new_grid[row, col] = 1
        
        self.grid = new_grid
        self.generation += 1
        
    def randomize(self, density: float = 0.3):
        """
        Llena el tablero con células vivas de forma aleatoria.
        
        Args:
            density: Densidad de células vivas (entre 0 y 1).
        """
        self.grid = np.random.choice([0, 1], size=(self.rows, self.cols), 
                                     p=[1 - density, density])
        self.generation = 0
        
    def clear(self):
        """Limpia el tablero, matando todas las células."""
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        self.generation = 0
        
    def load_pattern(self, pattern: List[Tuple[int, int]], offset_row: int = 0, offset_col: int = 0):
        """
        Carga un patrón predefinido en el tablero.
        
        Args:
            pattern: Lista de tuplas (fila, columna) con las posiciones de las células vivas.
            offset_row: Desplazamiento en filas desde la esquina superior izquierda.
            offset_col: Desplazamiento en columnas desde la esquina superior izquierda.
        """
        for row, col in pattern:
            self.set_cell(row + offset_row, col + offset_col, 1)
        self.generation = 0
        
    def get_live_cells(self) -> Set[Tuple[int, int]]:
        """
        Obtiene el conjunto de células vivas.
        
        Returns:
            Conjunto de tuplas (fila, columna) con las posiciones de las células vivas.
        """
        live_cells = set()
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row, col] == 1:
                    live_cells.add((row, col))
        return live_cells


def main():
    """Función principal para ejecutar el juego."""
    print("Juego de la Vida de Conway")
    print("==========================")
    
    # Configuración inicial
    rows = int(input("Introduce el número de filas (default: 30): ") or "30")
    cols = int(input("Introduce el número de columnas (default: 50): ") or "50")
    
    game = GameOfLife(rows, cols)
    
    # Patrones predefinidos
    patterns = {
        "Glider": [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        "Blinker": [(1, 0), (1, 1), (1, 2)],
        "Toad": [(1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2)],
        "Beacon": [(0, 0), (0, 1), (1, 0), (2, 3), (3, 2), (3, 3)],
        "Pulsar": [
            (2, 0), (2, 1), (2, 2), (2, 6), (2, 7), (2, 8),
            (4, 2), (4, 6),
            (5, 2), (5, 6),
            (6, 2), (6, 6),
            (7, 0), (7, 1), (7, 2), (7, 6), (7, 7), (7, 8),
            (9, 2), (9, 6),
            (10, 2), (10, 6),
            (12, 0), (12, 1), (12, 2), (12, 6), (12, 7), (12, 8)
        ]
    }
    
    # Menú de opciones
    while True:
        print("\nOpciones:")
        print("1. Colocar células manualmente")
        print("2. Generar células aleatorias")
        print("3. Cargar un patrón predefinido")
        print("4. Limpiar el tablero")
        print("5. Ejecutar simulación paso a paso")
        print("6. Ejecutar simulación continua")
        print("7. Salir")
        
        option = input("Selecciona una opción: ")
        
        if option == "1":
            # Colocar células manualmente
            game.display()
            print("Introduce las coordenadas de las células vivas (fila columna).")
            print("Introduce 'q' para terminar.")
            
            while True:
                cell_input = input("Coordenadas (fila columna): ")
                if cell_input.lower() == 'q':
                    break
                
                try:
                    row, col = map(int, cell_input.split())
                    game.toggle_cell(row, col)
                    game.display()
                except ValueError:
                    print("Entrada no válida. Introduce dos números separados por espacio.")
        
        elif option == "2":
            # Generar células aleatorias
            density = float(input("Introduce la densidad de células vivas (0-1, default: 0.3): ") or "0.3")
            game.randomize(density)
            game.display()
        
        elif option == "3":
            # Cargar un patrón predefinido
            print("Patrones disponibles:")
            for i, name in enumerate(patterns.keys(), 1):
                print(f"{i}. {name}")
            
            pattern_choice = input("Selecciona un patrón: ")
            try:
                pattern_index = int(pattern_choice) - 1
                pattern_name = list(patterns.keys())[pattern_index]
                pattern = patterns[pattern_name]
                
                # Calcular el offset para centrar el patrón
                offset_row = (game.rows - max(row for row, _ in pattern)) // 2
                offset_col = (game.cols - max(col for _, col in pattern)) // 2
                
                game.clear()
                game.load_pattern(pattern, offset_row, offset_col)
                game.display()
            except (ValueError, IndexError):
                print("Selección no válida.")
        
        elif option == "4":
            # Limpiar el tablero
            game.clear()
            game.display()
        
        elif option == "5":
            # Ejecutar simulación paso a paso
            game.display()
            input("Presiona Enter para continuar a la siguiente generación (q para salir): ")
            
            while True:
                game.next_generation()
                game.display()
                
                user_input = input("Presiona Enter para continuar (q para salir): ")
                if user_input.lower() == 'q':
                    break
        
        elif option == "6":
            # Ejecutar simulación continua
            delay = float(input("Introduce el retraso entre generaciones en segundos (default: 0.2): ") or "0.2")
            max_generations = int(input("Introduce el número máximo de generaciones (0 para infinito, default: 0): ") or "0")
            
            generation = 0
            try:
                while max_generations == 0 or generation < max_generations:
                    game.next_generation()
                    game.display()
                    time.sleep(delay)
                    generation += 1
            except KeyboardInterrupt:
                print("\nSimulación detenida.")
        
        elif option == "7":
            # Salir
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()