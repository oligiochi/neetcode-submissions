class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums: list[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        center = (left + right) // 2
        
        if nums[center] == target:
            return center
        
        # Se la parte sinistra è ordinata
        if nums[left] <= nums[center]:
            if nums[left] <= target < nums[center]:
                return self.binary_search(nums, target, left, center - 1)
            else:
                return self.binary_search(nums, target, center + 1, right)
        # Se la parte destra è ordinata
        else:
            if nums[center] < target <= nums[right]:
                return self.binary_search(nums, target, center + 1, right)
            else:
                return self.binary_search(nums, target, left, center - 1)