class Solution(object):
    def findDuplicate(self, nums):

        nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            if nums[i] == nums[i+1]:
                return nums[i]
        return -1


        