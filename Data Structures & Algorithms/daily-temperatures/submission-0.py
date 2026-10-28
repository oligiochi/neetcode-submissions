class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size=len(temperatures)
        output=[0]*size
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT,stackI=stack.pop()
                output[stackI]=(i-stackI)
            stack.append([t,i])
        return output
                
        