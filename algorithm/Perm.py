def perm(lis,begin,end): #调换顺序
    #print "调用perm函数"
    if begin>=end: #等到所有循环走完，直接进行输出
        print(lis)
    else:
        i = begin
        for num in range(begin,end):
            # print("i-->",i,"num-->",num)
            lis[num],lis[i] = lis[i],lis[num] #固定当前位置,在进行下一位的排列
            # print("list:   ",lis)
            perm(lis,begin+1,end) #在这一步就可以输出结果
            # 调用结束之后还需要回溯将交换位置的元素还原,以供其他下降路径使用(二叉树)
            # print("回朔:  num:   ",num,"i--->",i)
            lis[num],lis[i] = lis[i],lis[num]


lis = [1,2,3]
perm(lis,0,3)