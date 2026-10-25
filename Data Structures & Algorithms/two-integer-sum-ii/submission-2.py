class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1  # Due puntatori, uno all'inizio e uno alla fine
        
        while i < j:
            current_sum = numbers[i] + numbers[j]
            
            if current_sum == target:
                return [i + 1, j + 1]  # Restituisci gli indici in forma 1-based
            
            elif current_sum < target:
                i += 1  # Se la somma corrente è troppo piccola, sposta il puntatore sinistro
                
            else:
                j -= 1  # Se la somma corrente è troppo grande, sposta il puntatore destro
        
        return []  # Se non viene trovata una soluzione