class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappa={}
        for i,num in enumerate(nums):
            mappa[num]=i
        for i,num in enumerate(nums):
            pos=mappa.get(target-num,-1)
            if pos!=-1 and pos!=i:
                return [pos,i] if pos<i else [i,pos]