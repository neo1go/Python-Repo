# Leetcode 73
# Es sollen 0 gesetzt werden für ganze Zeilen oder Spalten, immer dann wenn in der Spalte oder Zeile eine 0 existiert.
# Der Trick ist, für die erste Spalte und erste Reihe bools zu setzen.
# Dann wird im zweiten Durchlauf ab index 1 für Zeilen und Spalten eine 0 als Marker gesetzt, also ein inneres Koordinatensystem.
# Jetzt wird die Matrix anhand dieser Marker ab index 1 komplett auf die Nullen gesetzt.
# Und am Ende werden die ersten Zeilen und Spalten anhand der bools noch gesetzt.
class Solution(object):
    """
    # Standard Variante
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        
        zero_rows = set()  # x Achse- Dies sind Hilfs Sets für die Koordinaten
        zero_cols = set()  # y Achse
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        # Zeile mit 0 ersetzen           
        for row in zero_rows: 
            for j in range(cols): # basierend auf dem Hilfsset wird hier alles auf null gesetzt
                matrix[row][j] = 0
        
        # Spalte mit 0 ersetzen
        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0
                
        return matrix
        """
        
    def set_zeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # bools setzen
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
        
        # Marker setzen 
        for i in range(1, rows): 
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0 # Zeilenmarker
                    matrix[0][j] = 0 # Spaltenmarker
                    
        # jetzt wird die Matrix genullt anhand der Maker, die kurz zuvor gesetzt wurden.      
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # hier wird am Ende die ganze Zeile oder Spalte genullt. Dies ist voher wegen einer möglichen Verfälschung verboten.            
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
                
        if first_col_has_zero:
            for i in range(rows):
                for i in range(rows):
                    matrix[i][0] = 0
                    
        return matrix
    
    
    
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print(Solution().set_zeroes(matrix))
