class Solution:
    def findMin(self, nums):
        min = nums[0]
        for num in nums:
            if num < min:
                min = num
        return min


mySolution = Solution()
print(mySolution.findMin([4,5,6,7,0,1,2]))