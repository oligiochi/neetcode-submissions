class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation={
            '+':self.sum,
            '*':self.mul,
            '/':self.div,
            '-':self.sotr,
        }
        keys=operation.keys()
        numberstack=[]
        for token in tokens:
            try:
                num=int(token)
                numberstack.append(num)
                #print(numberstack)
            except:
                pass
            if token in keys:
                b=numberstack.pop()
                a=numberstack.pop()
                numberstack.append(operation[token](a,b))
                
        return numberstack.pop();

    def sum(self,a,b):
        return a+b
    
    def sotr(self,a,b):
        return a-b
    
    def mul(self,a,b):
        return a*b
    
    def div(self,a,b):
        return int(a/b)