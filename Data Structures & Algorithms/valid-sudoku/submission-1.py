class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mappacelle = {i: {} for i in range(10)}
        mappacolonne=[]
        for j,riga in enumerate(board):
            mappariga={}
            for i,e in enumerate(riga):
                if i>=len(mappacolonne):
                    mappacolonne.append({})
                quadrante_idx = (j // 3) * 3 + (i // 3)
                if e!='.':
                    if e in mappacolonne[i]:
                        return False
                    if e in mappariga:
                        return False
                    if e in mappacelle[quadrante_idx]:
                        return False
                    mappacelle[quadrante_idx][e]=0
                    mappariga[e]=0
                    mappacolonne[i][e]=0
        return True
        