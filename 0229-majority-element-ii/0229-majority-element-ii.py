class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        mp = {}
        threshold = len(nums)//3
        res = []
        
        for num in nums:
            mp[num] = mp.get(num, 0) + 1

        for num in mp:
            if mp[num] > threshold:
                res.append(num)
        
        return res                