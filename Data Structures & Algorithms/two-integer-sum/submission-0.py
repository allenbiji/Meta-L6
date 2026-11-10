class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i, val in enumerate(nums):
            diff = target - val 
            if diff in sums:
                return [sums[diff], i]
            sums[val] = i
        