class Solution(object):

    def __init__(self):
        self.strlist= []
        self.result = []
    def findSubstring(self, s, words):
        # result = []
        self.permutation(words, 0)
        mySet = set(self.strlist)
        for str in mySet:
            # print('quanpailiestr-->',str)
            # print(s)
            if str in s:
                print("in str:", str)
                print("newString:", s.replace(str, " "))
                index = s.replace(str, " ").index(" ")
                self.result.append(index)
        return self.result
    def permutation(self,s,i):
        if i == len(s):
            self.strlist.append(''.join(s))
            # print("quanpailie   ",s)
        else:
            for j in range(i, len(s)):
                s[j], s[i] = s[i], s[j]
                self.permutation(s, i + 1)
                s[j], s[i] = s[i], s[j]

        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
ss = 'barfoothefoobarman'
words = ["foo", "bar"]
ss1 = "barfoofoobarthefoobarman"
words1=["bar","foo","the"]
ss2 = "wordgoodgoodgoodbestword"
words2 = ["word","good","best","good"]
ss3 = "foobarfoobar"
words3 = ["foo","bar"]
so  = Solution()

ret = so.findSubstring(ss3,words3)
for str in so.strlist:
    print("str---->",str)
for i in ret:
    print("i--->",i)

