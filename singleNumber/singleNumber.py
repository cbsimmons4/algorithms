class Solution:
    def singleNumber(self, nums):
        single = set()
        for num in nums:
            if num not in single:
                single.add(num)
            else:
                single.remove(num)
        return list(single)


mySolution = Solution()
print(mySolution.singleNumber([2,1,2,3,4,1]))