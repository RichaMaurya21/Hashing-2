'''## Problem3 (https://leetcode.com/problems/longest-palindrome)
Created a hashset. Check it character is present, if not present add character, if present increase result with 2 that means there are 2 character and then remopve it .
At the end when all character traversed and hashset is still not empty then add 1 extra to result. Because palaindrome can have only 1 odd character in it. '''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = set()
        res = 0
        for i in s:
            if i not in hashset:
                hashset.add(i)
            else:
                res += 2
                hashset.remove(i)
            
        if hashset:
            res = res + 1
        
        return res


sol = Solution()
nums = 'abccccdd'
print(sol.longestPalindrome(nums))