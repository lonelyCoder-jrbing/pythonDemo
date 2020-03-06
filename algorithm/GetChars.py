# def getChars(length):
#     return [getChar(index) for index in range(length)]
#
#
# def getChar(number):
#     # if number < 9:
#     mydict = {}
#     factor, moder = divmod(number, 26)  # 26 字母个数
#     # else:
#     #     factor, moder = divmod(number, 26)
#     #     factor, moder = factor, moder + '#'
#     #     print()
#     # print("factor,moder  ", factor, moder)
#     if moder < 9:
#         modChar = chr(moder + 65)  # 65 -> 'A'
#     else:
#         modChar = chr(moder + 65) + '#'
#     print("modchar:   ", modChar)
#     if factor != 0:
#         modChar = getChar(factor - 1) + modChar  # factor - 1 : 商为有效值时起始数为 1 而余数是 0
#     mydict[modChar.lower()] = moder
#     return mydict
#
#
# def toLowerCase(str):
#     strList = list(str)
#     for i, j in enumerate(strList):
#
#         if j >= 'A' and j <= 'Z':
#             strList[i] = chr(ord(j) + ord('a') - ord('A'))
#     return "".join(strList)
#
#
# chars = getChars(26)
#
# print(chars)
#
# s = "10#11#12"
# ssss = s.split('#')
# for n in ssss:
#
#     if n > 26:
#         fen = list[n]
#
# print(ssss)


class Solution(object):
    def __init__(self):
        self.string = ''
        self.newList = []

    def freqAlphabets(self, s):
        mylist = s.split('#')
        print("mylist:  ", mylist)

        for i in range(0,len(mylist)):
            if i<len(mylist)-1:
                if int(mylist[i])>26 and int(mylist[i])<100:
                    self.newList.extend(list(int(mylist[i])))



        for number in self.newList:
            print("number:  ", number)
            self.string += chr(int(number) + 64).lower()
            print("chr:  ", chr(int(number) + 64).lower())
        return self.string


"""
:type s: str
:rtype: str
"""
ss1 = "10#11#12"
so = Solution()
retss = so.freqAlphabets(ss1)
print("ret:", retss)
