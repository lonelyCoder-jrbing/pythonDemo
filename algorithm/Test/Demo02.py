from functools import reduce
import operator


class DemoForBeautifulArr(object):
    def beautifulArr(self, N):
        alist = []
        ret = []
        v = int(N / 2)
        for i in range(1, N + 1):
            alist.append(i)
        print("alist:  ", alist)
        for j in range(0, N):
            temInt = N - 1 - j
            if j < temInt:
                ret.append(alist[j])
            if temInt >= v:
                ret.append(alist[temInt])
            else:
                return ret

    def beautifulArr01(self, N):
        lst = [[n for n in range(1, N + 1)]]
        copy = []
        while len(lst[0]) > 2:
            for l in lst:
                print("l==>",l)
                copy.append([l[i] for i in range(0, len(l), 2)])
                print("copy01===>",copy)
                copy.append([l[i] for i in range(1, len(l), 2)])
                print("copy02===>",copy)
            lst = copy.copy()
            copy = []
        return reduce(operator.add, lst)


so = DemoForBeautifulArr()
result01 = so.beautifulArr01(10)
result = so.beautifulArr(5)
print("result01:  ", result01)
print("result:  ", result)

#先进行排序,然后再找出排序好的下标为k-1的值,做为标志
class Solution(object):
    def kClosest(self, points, K):
        aqList = []
        aMap = {}
        result = []
        for i in range(0,len(points)):
            aqList.append(points[i][0]**2+points[i][1]**2)
            # aMap[i] = points[i][0]**2+points[i][1]**2
            # aqList.append()
        aqList.sort()
        markValue = aqList[K-1]
        for i in range(0,len(points)):
            if markValue>=points[i][0]**2+points[i][1]**2:
                result.append(points[i])
        return result
        # import operator
        # print("aMap-====>",aMap)
        # aMap =  sorted(aMap.items(),key=operator.itemgetter(1))
        # print("sorted:   ",aMap)
        # # # aqList.sort()
        # # noMap = {aMap[i] for i in range(0, K)}
        # # print("noMap-->",noMap)
        # for j in list(aMap[num][0] for num in range(0,K)):
        #     print("j====>",j)
        #     aqList.append(points[j])
        # return aqList

so = Solution()
points = [[2,5],[1,2],[1,3],[2,3],[2,4],[1,1]]
result  = so.kClosest(points,3)
print("result---:  ",result)


# lst = [1,3,2,5,6]
# lst.sort()
# print(lst)


