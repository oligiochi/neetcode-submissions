class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # Controlla se la matrice è vuota
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1  # Inizializza gli indici per la ricerca binaria
        
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // n][mid % n]  # Calcola il valore medio
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False