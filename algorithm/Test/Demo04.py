class Solution01(object):
    def getZeroNum(self, n):
        ret = self.trailingZeroes(n)
        # print("jiehceng ", ret)
        string = str(ret)
        # print("string=", string)
        zeroNum = 0

        # print(string[i])
        # print("--->", len(string) - 1 - i)
        i = len(string) - 1
        while string[i] == '0' and i >= 0:
            i -= 1
            zeroNum += 1
        return zeroNum

    def trailingZeroes(self, n):
        if n > 2:
            return n * self.trailingZeroes(n - 1)
        elif n == 2:
            return n * 1


import math


class Solution(object):
    def trailingZeroes(self, n):
        return 2 * math.floor(n / 25) + math.floor(n / 5) - math.floor(n / 25)


for i in range(0, 5):
    print("pow(5,i)--------------------------->",i)
    so01 = Solution01()
    ret01 = so01.getZeroNum(pow(5,i))
    print("ret01:   ", ret01)
    so = Solution()
    ret = so.trailingZeroes(pow(5,i))
    print("ret: ", ret)
