class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        maj_ele = n//2
        hmap_cnt = {}

        for num in nums:
            hmap_cnt[num] = hmap_cnt.get(num, 0) + 1

            if hmap_cnt[num] > maj_ele:
                return num

        return -1
