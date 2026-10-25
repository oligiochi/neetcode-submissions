class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        key=[]
        for num in nums:
            if num in key:
                return True
            else:
               key.append(num)
        return False