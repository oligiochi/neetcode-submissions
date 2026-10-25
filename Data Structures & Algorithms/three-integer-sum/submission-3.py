class Solution:
    def sumEqualzero(self,n1,n2,n3):
        return n1+n2+n3==0

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negArr,zeroArr,posArr=[],[],[]
        sortNums=sorted(nums)
        ritorno=set()
        
        for n in sortNums:
            if n<0:
                negArr.append(n)
            elif n==0:
                zeroArr.append(n)
            else:
                posArr.append(n)
        if len(zeroArr)<3:
            if (not negArr and posArr) or (negArr and not posArr):
                return []
        else:
            #result = comb(len(zeroArr), 3)
            ritorno.add(tuple([0, 0, 0])) # [for _ in range(result)]
        posArr.reverse()
        nCicli=posArr if len(posArr)<=len(negArr) else negArr
        altro=posArr if len(posArr)>len(negArr) else negArr
        # Prima passata
        for n in nCicli:
            seen = set()  # Per tenere traccia dei duplicati
            for j in range(len(altro)):
                if altro[j] in seen:
                    continue  # Salta i duplicati
                seen.add(altro[j])
                
                if self.sumEqualzero(n, altro[j], 0) and zeroArr:
                    ritorno.add(tuple(sorted([n, altro[j], 0])))  # Aggiungi tripla ordinata

                for k in range(len(altro)):
                    if k != j and self.sumEqualzero(n, altro[j], altro[k]):
                        ritorno.add(tuple(sorted([n, altro[j], altro[k]])))  # Aggiungi tripla ordinata

        # Seconda passata
        for n in altro:
            seen = set()  # Resetta per la nuova iterazione
            for j in range(len(nCicli)):
                if nCicli[j] in seen:
                    continue  # Salta i duplicati
                seen.add(nCicli[j])
                
                if self.sumEqualzero(n, nCicli[j], 0) and zeroArr:
                    ritorno.add(tuple(sorted([n, nCicli[j], 0])))  # Aggiungi tripla ordinata

                for k in range(len(nCicli)):
                    if k != j and self.sumEqualzero(n, nCicli[j], nCicli[k]):
                        ritorno.add(tuple(sorted([n, nCicli[j], nCicli[k]])))  # Aggiungi tripla ordinata
        
        risultato_lista = [list(tupla) for tupla in ritorno]
        return risultato_lista
