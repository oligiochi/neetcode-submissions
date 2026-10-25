import random
import math

class Parantisi:
    def __init__(self):
        self.isaperta=False
        self.iscompleta=False
    def apriparentesi(self)->str:
        if not self.isaperta:
            self.isaperta=True
            return "("
        else:
            return ""
    def chiudiparentesi(self)->str:
        if self.isaperta:
            #self.isaperta=False
            self.iscompleta=True
            return ")"
        else:
            return ""
    def is_completa(self)->bool:
        return self.iscompleta
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        parentesi=[]
        counter=0
        catalan_number=math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
        print(catalan_number)
        while len(stack)<catalan_number:
            for _ in range(n):
                p = Parantisi()
                parentesi.append(p)
            mystr=""
            while not all(p.is_completa() for p in parentesi):
                numero = random.choice([0, 1])
                p=random.choice(parentesi)
                if numero == 0:
                    mystr += p.apriparentesi()  # Usa += per concatenare
                else:
                    mystr += p.chiudiparentesi()  # Usa += per concatenare
                if p.is_completa():
                    parentesi.remove(p)
            #print(mystr)
            if mystr not in stack:
                stack.append(mystr)
        return stack
