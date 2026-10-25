class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        reverse=nums[::-1]
        multD,multR=[1]*len(nums),[1]*len(nums)
        for i in range(1,len(nums)):
            multD[i]=multD[i-1]*nums[i-1]
            multR[i]=multR[i-1]*reverse[i-1]
        for i,item in enumerate(multR[::-1]):
            multD[i]=multD[i]*item
        return multD
        