#找出最大值和最小值 然后再创建一个数组  数组的长度就是最大值减去一
class solution(object):
    def __init__(self):
        arr = []
    def colorClassifition(self,arrays):
        maxNum = arrays[0]
        minNum = arrays[0]
        for i in arrays:
            if i>maxNum:
                maxNum = i
            if i<minNum:
                minNum = i



        print("maxNum:",maxNum)
        print("minNum:",minNum)
so  = solution()
arr = [0,0,0,2,1,2,1,0,1]
so.colorClassifition(arr)

