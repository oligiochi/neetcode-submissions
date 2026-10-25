class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seenNums:
                return [seenNums[diff], i]
            seenNums[n] = i
