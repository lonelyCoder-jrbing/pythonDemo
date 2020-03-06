class Solution(object):
    def __init__(self):
        self.retList = []

    def permuteUnique(self, nums):

        stack = []
        self.perm(nums, stack)
        print("result list:===>",self.retList)
        return self.retList

    def perm(self, alist, stack):
        j = 0
        if not alist:
            print("line4 ", stack)  # 到树的最后，输出结果
            self.retList.append(stack)
            print("append stack:   ",self.retList)
        else:  # 没有到树的叶子节点的时候，使用递归继续往下找。
            size = len(alist)
            for i in range(size):
                print("line7, stack.append(alist[i])  ", alist[i], " i value: ", i)
                stack.append(alist[i])
                del alist[i]
                print("line10, stack:  ", stack, "alist:   ", alist)
                j += 1
                print("line12, before perm  j=", j)
                self.perm(alist, stack)
                j -= 1
                print("line15, after perm   j=", j)
                el = stack.pop()
                # print("insert index-->",i)
                print("line18,   the outer element in stack;  ", el)
                alist.insert(i, el)
                print("line20,   alist after insert into:   ", alist, "insert index-->", i)


so = Solution()
nums = [1,1,2]
result = so.permuteUnique(nums)
print("result===>",result)