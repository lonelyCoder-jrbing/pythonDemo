class Solution(object):
    def __init__(self):
        # 数字的全排列的集合
        self.s = []
        self.i = 0

    def beautifulArray(self, s, i):

        if i == len(self.s):
            # print(s)
            for numberOne in range(0, len(self.s)):
                for numberTwo in range(numberOne, len(self.s)):
                    for j in range(numberOne, numberTwo):
                        if 2 * self.s[j] is not self.s[numberOne] + self.s[numberTwo]:
                            self.alist.append(i)
        else:
            for j in range(i, len(self.s)):
                self.s[j], self.s[i] = self.s[i], self.s[j]
                self.beautifulArray(self.s, i + 1)
                self.s[j], self.s[i] = self.s[i], self.s[j]

    def operate(self, N):
        for num in range(1, N):
            self.s.append(num)
        self.beautifulArray(self.s, self.i)


class allSort():
    def __init__(self):
        self.allList = []

    def perm(self, lis, begin, end):  # 调换顺序
        # print "调用perm函数"
        if begin >= end:  # 等到所有循环走完，直接进行输出
            # print(lis)
            self.allList.append(''.join([str(x) for x in lis]))
            # print("appended---->",self.allList)
        else:
            i = begin
            for num in range(begin, end):
                lis[num], lis[i] = lis[i], lis[num]  # 固定当前位置,在进行下一位的排列
                self.perm(lis, begin + 1, end)  # 在这一步就可以输出结果
                # 调用结束之后还需要回溯将交换位置的元素还原,以供其他下降路径使用(二叉树)
                lis[num], lis[i] = lis[i], lis[num]
        return self.allList

    # 拿到N之后,得到的1~N之间的值,
    def beautifulArray(self, N):
        alist = []
        beautiList = []
        for num in range(1, N + 1):
            alist.append(num)
        allRawList = self.perm(alist, 0, N - 1)
        # print("allRawList:   ",allRawList)
        for lists in allRawList:
            flag = True
            print("String=====>", lists)
            for i in range(0, len(lists)):
                for j in range(i, len(lists)):
                    for k in range(i + 1, j):
                        # print("i====>", i, "charAt[i]:", lists[i])
                        # print("j====>", j, "charAt[j]:", lists[j])
                        # print ("k===>",k,"charAt[k]:",lists[k])
                        if 2 * int(lists[k]) == int(lists[i]) + int(lists[j]):
                            print("make some change........")
                            flag = False
            print("flag----->", flag)
            if flag is True:
                beautiList.append(lists)
        if beautiList:
            return list([int(x) for x in beautiList[0]])
        else:
            return []


#
# alist = [1,2,3,4]
# all = allSort()
# ret = all.beautifulArray(9)
# print("ret==>",ret)


# 算法复杂度过高,求出全排列会很耗时,
class nicerSolution():
    def __init__(self):
        # self.lis = []
        self.ret = []

    # 获取到1-N的数组
    def beautifulArray(self, N):
        lis = []
        for i in range(1, N + 1):
            lis.append(i)
        begin = 0
        end = N
        return self.transfer(lis, begin, end)

    def transfer(self, lis, begin, end):  # 调换顺序
        # print "调用perm函数"
        flag = True
        m = 0
        if begin >= end and m == 0:  # 等到所有循环走完，直接进行输出
            m += 1
            print(lis)
            print("String=====>", lis)
            for i in range(0, len(lis)):
                for j in range(i, len(lis)):
                    for k in range(i + 1, j):
                        print("i====>", i, "charAt[i]:", lis[i])
                        print("j====>", j, "charAt[j]:", lis[j])
                        print("k===>", k, "charAt[k]:", lis[k])
                        if 2 * int(lis[k]) == int(lis[i]) + int(lis[j]):
                            print("make some change........")
                            flag = False
                            break
                if i == len(lis) - 1 and flag is True:
                    print("lis:   ", lis)
                    self.ret = lis
                    return lis
            print("flag----->", flag)
            # if flag is True and m>0:
            #    self.ret = lis
        # elif flag is True and m>0:
        #     return self.ret
        else:
            i = begin
            for num in range(begin, end):
                lis[num], lis[i] = lis[i], lis[num]  # 固定当前位置,在进行下一位的排列
                resukt = self.transfer(lis, begin + 1, end)  # 在这一步就可以输出结果
                if resukt:
                    return resukt
                # 调用结束之后还需要回溯将交换位置的元素还原,以供其他下降路径使用(二叉树)
                lis[num], lis[i] = lis[i], lis[num]


# nicer = nicerSolution()
# # midRet = nicer.transfer(5)
# # print("midRet:    ",midRet)
# arr  = nicer.beautifulArray(4)
# print(arr)


class Solution:
    def beautifulArray(self, N):
        memo = {1: [1]}
        def f(N):
            if N not in memo:
                odds = f((N + 1) / 2)
                evens = f(N / 2)
                memo[N] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
            return memo[N]
        return f(N)


# so = Solution()
# so.beautifulArray(4)

# from list import List
#打散法
class nicerSolution:
    def beautifulArray(self, N: int):
        recursiveMark = 0
        def _helper(nob_list):
            # recursiveMark+=1
            # print("",recursiveMark)
            if len(nob_list) <= 2:
                return nob_list
            b1 = _helper(nob_list[::2])   #从零开始截取,步长是2
            print("nob_list:   ",nob_list)
            print ("b1:  ",b1)
            b2 = _helper(nob_list[1::2])  #从1开始截取,步长是2
            print("b2:   ",b2)
            return b1 + b2
        n_list = list(range(1, N+1))
        print("n_list:   ",n_list)
        beatiful_list = _helper(n_list)
        return beatiful_list
so = nicerSolution()
ret  = so.beautifulArray(9)

print ("result :  ",ret)