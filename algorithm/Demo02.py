list = []
def permutation(s,i):
    if i == len(s):
        list.append(''.join(s))
        print(s)
    else:
        for j in range(i,len(s)):
            s[j],s[i] = s[i],s[j]
            permutation(s,i+1)
            s[j],s[i] = s[i],s[j]



def getIndexFromString(stringss,lists):

    result = []
    permutation(lists,0)
    for str in list:
        print(str)
        print(stringss)
        if str in stringss:
            print ("str:",str)
            print ("newString:",stringss.replace(str," "))
            index =  stringss.replace(str," ").index(" ")


            # print(index)
            result.append(index)
    return  result

ss00 = 'jrbingjurongbingzmiwanttoeat'
words00 = ["jrbing", "jurongbing", "zm"]
ss = 'barfoothefoobarman'
words = ["foo", "bar"]
ret = getIndexFromString(ss00,words00)
for i in ret:
    print(i)















