class Solution:
    def maxSubArray(self, nums):
        curr_sum = 0
        maxi = float('-inf')

        for i in range(len(nums)):
            curr_sum += nums[i]
            maxi = max(maxi, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return maxi