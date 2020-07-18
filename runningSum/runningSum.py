class Solution:
    def runningSum(self, nums):
        if (len(nums) <= 1): return nums
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums

mySolution = Solution()
print(mySolution.runningSum([1,2]))


