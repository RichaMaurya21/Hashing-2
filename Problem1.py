## Problem1 (https://leetcode.com/problems/subarray-sum-equals-k/)


class Solution:
    def subarraySum(self, nums, k):
        dic = {0: 1}  # Initialize with 0:1 to handle the case when the subarray starts from the beginning
        res = 0
        count = 0
        for i in nums:
            res += i
            # y = x - z
            if (res - k) in dic:
                count += dic[res - k]
            dic[res] = dic.get(res, 0) + 1

        return count

sol = Solution()
nums = [3,4,7,2,-3,1,4,2,0,1]
k = 7
print(sol.subarraySum(nums,k))