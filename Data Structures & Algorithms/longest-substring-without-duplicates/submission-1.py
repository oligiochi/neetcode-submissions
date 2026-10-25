class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Set per tenere traccia dei caratteri nella sottostringa corrente
        l = 0  # Indice sinistro della finestra scorrevole
        max_len = 0  # Lunghezza massima della sottostringa non ripetuta

        for r in range(len(s)):  # Indice destro della finestra scorrevole
            while s[r] in char_set:  # Se il carattere è già nel set, muovi il puntatore sinistro
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])  # Aggiungi il carattere al set
            max_len = max(max_len, r - l + 1)  # Aggiorna la lunghezza massima

        return max_len
