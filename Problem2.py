'''## Problem2 (https://leetcode.com/problems/contiguous-array/)
So here I am using concept taught in class that z = x-y where x = running sum till last, y is the first most running sum from where subarray starts, if the running sum at y and  x is same i.e x= 5 and y =5
that means z = 0, hence subarray between y and x i.e z will be the subarray to return'''  

class Solution:
    def findMaxLength(self, nums):
        dic = {0: -1}
        max_length = 0
        resSum = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                resSum += 1
            else:
                resSum += -1
            # Check if the current cumulative sum has been seen before
            if resSum in dic:
                 # If yes, update the maximum length of subarray
                max_length = max(max_length, i - dic[resSum]) #(maxLength or (x-y))
            else:
                # If no, store the index of the current cumulative sum
                dic[resSum] = i
        
        return max_length


sol = Solution()
nums = [1,0,0,1,1,1,1,1,0,0,0,0,0,1]
print(sol.findMaxLength(nums))