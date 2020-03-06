# # 利用子字符串寻找在大的字符串中子字符串第一次匹配的位置
# # 定义一个窗口的长度 字串的长度
# import math
#
# bigStr = "ilovechinaiwanttobesuperman"
# littleStr = 'want'
# newStr = bigStr.replace(littleStr, "")
# print(newStr)
#
# for i in range(0, len(bigStr) - 1):
#     # print(bigStr[i:i + len(littleStr)])
#     if bigStr[i:i + len(littleStr)] == littleStr:
#         print(i)
#
# for i in range(0, 0):
#     print("rang---->", i)
#
# jrbing = ""
# if jrbing == "":
#     print("yes")
#
# # 将指定下标的字符串进行截取
#
# mystr = "iamjurongambingwant"
# newlen = len(mystr) / 2
# print("newlen", newlen)
# mylist = []
# for i in range(0, math.floor(newlen)):
#     my = mystr[2 * i:2 * i + 2]
#     mylist.append(my)
#
# for str in mylist:
#     print("str ", str)
#
# newStr = mystr[0:2]
# print("newstr == ", newStr)
#
# # 2,5
# mystr = mystr.replace("am", "", 1)
# print(mystr)
#
# mylist = []
# print("myList:", len(mylist))
# if len(mylist) == 0:
#     print("zero")
#
# f = 10.2
# i = int(f)
# print("i  ", i)
#
#
# def getChars(length):
#     return [getChar(index) for index in range(length)]
#
#
# def getChar(number):
#     if number < 9:
#         factor, moder = divmod(number, 26)  # 26 字母个数
#         print("factor,moder  ", factor, moder)
#
#     modChar = chr(moder + 65)  # 65 -> 'A'
#     print("modchar:   ", modChar)
#     if factor != 0:
#         modChar = getChar(factor - 1) + modChar  # factor - 1 : 商为有效值时起始数为 1 而余数是 0
#     return modChar
#
#
# chars = getChars(9)
# print(chars)
#
#
# def toLowerCase( str):
#     strList = list(str)
#     for i, j in enumerate(strList):
#
#         if j >= 'A' and j <= 'Z':
#             strList[i] = chr(ord(j) + ord('a') - ord('A'))
#     return "".join(strList)
# str = "IAMJURONGBING"
# lowercase  = toLowerCase(str)
# print(lowercase)
#
#
#
#
#


c = 'a'
print ("c---->",ord(c))
c1 = 'A'
ch = ord(c)
ch1 = ord(c1)+32
chars  =chr(ord(c1)+32)
print("chars:  ",chars)
print("A--->",ch1)
print ("a---->",ch)



zzz = 'Z'
zzzvalue  = ord(zzz)
print ("zzzvalue;   ",zzzvalue)



print("&---->",ord('&'))