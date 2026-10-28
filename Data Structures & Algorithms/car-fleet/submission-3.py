class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        map_car=[0]*target
        for p,s in zip(position,speed):
            map_car[p]=s

        for i in range(target-1,-1,-1):
            if map_car[i]==0:
                continue
            temp=(target-i)/map_car[i]
            if not stack:
                stack.append(temp)
            elif temp>stack[-1]:
                stack.append(temp)
            
        return len(stack)
