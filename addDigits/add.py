class Solution:
    def addDigits(self, num):
        cur = str(num)
        while (int(cur)/10) >= 1:
            nextCur = 0
            for c in cur:
                nextCur += int(c)
            cur = str(nextCur)
        return cur

mySolution = Solution()
print(mySolution.addDigits(9))