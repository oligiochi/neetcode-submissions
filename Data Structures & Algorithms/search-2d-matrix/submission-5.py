class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:  # Controlla se la matrice è vuota
            return False
        
        # Se c'è solo una riga, controlla direttamente quella riga
        if len(matrix) == 1:
            return self.searchArray(matrix[0], target)

        centro = len(matrix) // 2
        
        # Se il target è inferiore al primo elemento della riga centrale
        if matrix[centro][0] > target:
            return self.searchMatrix(matrix[:centro], target)
        
        # Se il target è superiore all'ultimo elemento della riga centrale
        if matrix[centro][-1] < target:
            return self.searchMatrix(matrix[centro + 1:], target)  # Escludi la riga centrale
        
        # Controlla se il target è presente nella riga centrale
        return self.searchArray(matrix[centro], target)

    def searchArray(self, array: List[int], target: int) -> bool:
        if not array:  # Controlla se l'array è vuoto
            return False
        
        # Se c'è solo un elemento, controlla se è il target
        if len(array) == 1:
            return array[0] == target
        
        centro = len(array) // 2
        
        # Ricerca binaria
        if array[centro] > target:
            return self.searchArray(array[:centro], target)
        elif array[centro] < target:
            return self.searchArray(array[centro + 1:], target)  # Escludi il centro
        else:
            return True  # Trovato