class Solution:
    def searchSF(self, nums, start, end, target):
        if start >= end:  # Se l'inizio supera o raggiunge la fine, significa che non abbiamo trovato l'elemento
            return -1
        
        centro = (start + end) // 2  # Calcola il centro dell'intervallo
        
        if target == nums[centro]:  # Se l'elemento al centro è il target, restituisci l'indice
            return centro
        
        if target < nums[centro]:  # Cerca nella metà sinistra
            return self.searchSF(nums, start, centro, target)
        else:  # Cerca nella metà destra
            return self.searchSF(nums, centro + 1, end, target)

    def search(self, nums, target):
        return self.searchSF(nums, 0, len(nums), target)
