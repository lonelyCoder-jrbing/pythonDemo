from typing import List
class Solution:
    # arr = []
    def __init__(self):
        self.arr = []
        self.num = []
        self.numArr = []
    def constructArray(self, n: int, k: int) -> List[int]:
        # 先初始化一个数组,计算其全排列,然后使用暴力算法进行排查
        arr = [i for i in range(1, n+1)]
        # print(arr)
        self.perm(arr, 0, n)
        print(" self.arr:   ",self.arr)
        length = len(self.arr)
        print("length:  ",length)
        for i in range(0,length):
            tempArr = []
            for j in range(1, n):
                tempArr.append((self.arr)[i][j] - (self.arr)[i][j-1])
            print("temparr: ",tempArr)
            if len(set(tempArr))==k:
                return self.arr[i]
    def perm(self, lis, begin, end):  # 调换顺序
        # print "调用perm函数"
        if begin >= end:  # 等到所有循环走完，直接进行输出
            self.arr.append(lis)
            print(lis)
        else:
            i = begin
            for num in range(begin, end):
                # print("i-->",i,"num-->",num)
                lis[num], lis[i] = lis[i], lis[num]  # 固定当前位置,在进行下一位的排列
                # print("list:   ",lis)
                self.perm(lis, begin + 1, end)  # 在这一步就可以输出结果
            # 调用结束之后还需要回溯将交换位置的元素还原,以供其他下降路径使用(二叉树)
            # print("回朔:  num:   ",num,"i--->",i)
            lis[num], lis[i] = lis[i], lis[num]
so  = Solution()
ret = so.constructArray(3,1)
print("ret:  ",ret)




#使用反转法进行求解
class solution02:
    def __init__(self):
        self.arr = []
    def constructArray(self,n:int ,k:int):
        self.arr = [i for i in range(0,n)]
        #如果k==1的时候直接返回
        if k==1:
            return  self.arr
        elif k>=1:
            for m in range(1,k):
                self.reverse(self.arr,m,n-1)
    def reverse(self,arr:list,i:int ,j:int):
        while i<j:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1

so02  = solution02()
res = so02.constructArray(4,2)
print("res:   ",res)

