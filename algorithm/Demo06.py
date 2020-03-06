# class Solution {
# public:
#     int search(vector<int>& nums, int target) {
#         int lo = 0, hi = nums.size() - 1;
#         while (lo < hi) {
#             int mid = (lo + hi) / 2;
#             if ((nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]))
#                 lo = mid + 1;
#             else
#                 hi = mid;
#         }
#         return lo == hi && nums[lo] == target ? lo : -1;
#     }
# };
#

class solution(object):

    def __init__(self):
        self.lower = 0
    def search(self,nums,target):
        lo = self.lower
        hi =len(nums)-1
        while(lo<hi):
            mid  = int((lo+hi)/2)
            if ((nums[0] > target) and (nums[0] > nums[mid]) and (target > nums[mid])):
                lo = mid + 1
            else:
                hi = mid
        if lo == hi and nums[lo] == target:
             return lo
        else:
             return -1
nums4 = [4, 5, 6, 7, 8, 1, 2, 3]
target4 = 8
so = solution()
result = so .search(nums4,target4)
print(result)



