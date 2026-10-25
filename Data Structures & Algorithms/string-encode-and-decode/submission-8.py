class Solution:
    def encode_string_to_number(self, s: str) -> str:
        # Codifica la stringa come byte UTF-8 e convertila in un numero intero
        return str(int.from_bytes(s.encode('utf-8'), 'big'))

    def decode_number_to_string(self, n: int) -> str:
        num_bytes = (n.bit_length() + 7) // 8
        return n.to_bytes(num_bytes, 'big').decode('utf-8')

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strings = tuple(strs)
        si = '?'.join(strings)
        return self.encode_string_to_number(si)

    def decode(self, s: str) -> List[str]:
        if not s:  # Gestisci il caso di stringa vuota
            return []
        sd = self.decode_number_to_string(int(s))
        if not sd: 
            return [""]
        return sd.split("?")