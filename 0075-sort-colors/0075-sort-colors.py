#Better Approach

class Solution:
    # Function to sort the array containing only 0s, 1s and 2s
    def sortColors(self, nums):
        # Initialize count variables for 0s, 1s, and 2s
        count0 = count1 = count2 = 0

        # Count the frequency of 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Fill with 0s
        for i in range(count0):
            nums[i] = 0

        # Fill with 1s
        for i in range(count0, count0 + count1):
            nums[i] = 1

        # Fill with 2s
        for i in range(count0 + count1, len(nums)):
            nums[i] = 2
