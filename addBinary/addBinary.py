class Solution:
    def addBinary(self, a, b):
        a10 = 0
        i = len(a) - 1
        k = 1
        while i >= 0:
            if a[i] == '1':
                a10 += k
            i = i - 1
            k = k*2
        b10 = 0
        i = len(b) - 1
        k = 1
        while i >= 0:
            if b[i] == '1':
                b10 += k
            i = i - 1
            k = k*2
        res = ""
        c10 = a10 + b10
        if c10 == 0: return "0"
        k = 1
        while c10 > 0:
            if (c10 & 1 == 1):
                res = "1" + res
            else:
                res = "0" + res
            c10 = c10 >> 1
        return res

mySolution = Solution()
print(mySolution.addBinary("0","1"))