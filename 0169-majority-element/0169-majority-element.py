class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        n = len(nums_sorted)
        return nums_sorted[n // 2]