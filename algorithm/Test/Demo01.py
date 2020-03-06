alist = [1, 0, 2]

for i in range(0, len(alist)):
    for j in range(i, len(alist)):
        if alist[i] < alist[j]:
            alist[i], alist[j] = alist[j], alist[i]
print(alist)

print(alist[2])

print(alist[::2])

print(divmod(12, 10))

print(len(str(34)))


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if list(str(nums[i]))[0] < list(str(nums[j]))[0]:
                    nums[i], nums[j] = nums[j], nums[i]
                elif  list(str(nums[i]))[0] == list(str(nums[j]))[0] :
                    if nums[i]>nums[j]:
                        if list(str(nums[i])[len(nums[j])-1,len(nums[i])-1])[0]<nums[j]:
                            nums[i], nums[j] = nums[j], nums[i]








        return "".join([str(i) for i in nums])


# 如果都相同,那么比较下一个数字和前一个值相比大小
nums = [121, 12]
so = Solution()
ret = so.largestNumber(nums)
print(ret)


