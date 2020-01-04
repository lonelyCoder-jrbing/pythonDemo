class caculate:
    def __init__(self, *args, **kwargs):
        self.name = ""
        self.num = [1,2,3]

    def permutation(self,nums, p, q):

        if p == q:
            s.append(list(nums))
        else:
            for i in  range(p,q):
                nums[i], nums[p] = nums[p], nums[i]
                self.permutation(nums, p + 1, q)
                nums[i], nums[p] = nums[p], nums[i]
        s = []
        nums = [i for i in range(1, 4)]
        self.permutation(nums, 0, len(nums))
        print(s)
if __name__ == "__main__":
    instance =  caculate()
    print(instance.num)
    instance.permutation(instance.num,0,2)


