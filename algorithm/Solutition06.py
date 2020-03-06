class Solution(object):
    def __init__(self):
        self.strlist = []
        self.result = []
    def findSubstring(self, s, words):
        # result = []
        if len(words) > 0:
            le = len(words[0])
        wordsLen = len(words)
        sle = len(s)
        if len(words) == 0:
            return []
        for i in range(0, sle):
            # print("第", i, "次")
            if i + wordsLen * le <= sle:
                newstr = s[i:i + wordsLen * le]
                mylist = []
                newlen = len(newstr) / le
                for j in range(0,int(newlen)):
                    my = newstr[le * j:le * (j + 1)]
                    mylist.append(my)
                # print("newstr= ", newstr)
                # print("mylsit :  ", mylist)
                # print("chang= ", i + len(words) * len(words[0]))
                for str in words:
                    # print("str-->", str)
                    if str in mylist:
                        # print("replaced str", str)
                        mylist.remove(str)
                        # newstr = newstr.replace(str, "", 1)
                    # print("myList  ", mylist)
                if len(mylist) == 0:
                    # print("appendi-->", i)
                    self.result.append(i)
                    # print("self.result:",self.result)
        return self.result
so = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
ret = so.findSubstring(s,words)
for i in ret:
    print("reti :  ",i)



