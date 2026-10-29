class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        i=0
        h=0
        j=len(heights)-1
        while i<j:
            base=j-i
            h=min(heights[i],heights[j])
            if heights[i]>heights[j]:
                h=heights[j];
                j-=1
            else:
                h=heights[i];
                i+=1
            area=base*h
            if area>maxArea:
                maxArea=area
        return maxArea

