class Solution:
    def longestSubarray(self, nums, limit):
        sub_min = nums[0]
        sub_max = nums[0]
        i = 0
        j = 0
        cur = 0
        max_len = 1

        for num in nums:
            if cur <= limit:
                i += 1
                if ((i - j) + 1) > max_len: 
            else:
                j += 1

                
