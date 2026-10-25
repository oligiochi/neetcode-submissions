import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = np.array(nums)
        sotr=target-arr
        sotr=sotr.tolist()
        sol=[]
        for i,item in enumerate(nums):
            temp = sotr[:i] + sotr[i+1 :]
            if item in temp:
                sol.append(i)
        return sol
        
        