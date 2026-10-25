class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        if(len(nums)==2):
            return nums[0] if nums[0]<nums[1] else nums[1]
        centro=len(nums)//2
        if(nums[0]<nums[-1]):
            return nums[0]
        if nums[centro]>nums[-1]:
            return self.findMin(nums[centro+1:])
        else:
            return self.findMin(nums[:centro+1])