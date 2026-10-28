class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        maxPI=position.index(max(position))
        stack=[(target-position[maxPI])/speed[maxPI]]
        combined = []
        for p,s in zip(position,speed):
            combined.append((p, s))

        combined = sorted(combined, key=lambda element: element[0])
        combined=combined[::-1]
        for p,s in combined:
            temp=(target-p)/s
            if temp>stack[-1]:
                stack.append(temp)
        return len(stack)
