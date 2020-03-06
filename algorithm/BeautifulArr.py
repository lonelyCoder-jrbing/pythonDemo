class nicerSolution():
    def __init__(self):
        self.lis = []
        self.ret = []

    # 获取到1-N的数组
    def transfer(self, N):
        for i in range(1, N + 1):
            self.lis.append(i)

    def beautifulArray(self, lis):  # 调换顺序
        # print "调用perm函数"
        flag = True
        m = 0
        len_list = len(lis)
        if len_list == 1:
            # return li
            # if begin >= end and  m==0:  # 等到所有循环走完，直接进行输出
            m += 1
            print(lis)
            print("String=====>", lis)
            if flag is True and m > 0:
                self.ret = lis
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
        if flag is True and m > 0:
            return self.ret
        result = []
        for i in range(len_list):
            res_list = lis[:i] + lis[i + 1:]
            s = lis[i]
            per_result = self.beautifulArray(res_list)
            if len(per_result) == 1:
                result.append(lis[i:i + 1] + per_result)
            else:
                result += [[s] + j for j in per_result]
                print("result:  ",result)
        return result
nicer = nicerSolution()
nicer.transfer(4)
# print(nicer.lis)
arr  = nicer.beautifulArray(nicer.lis)
print("arr:   ",arr)