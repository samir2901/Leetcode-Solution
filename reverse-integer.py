'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
'''

class Solution:
    def reverse(self, x: int) -> int:        
        if x < 0:
            num = self.reverseUtils(x*-1)*-1
        else:
            num = self.reverseUtils(x)
        
        if num >= -2**31 and num <= 2**31 - 1:
            return num 
        else:
            return 0
    
    def reverseUtils(self,x):
        rev_num = 0
        while x > 0:
            rev_num = rev_num*10 + x%10
            x = x//10 
        return rev_num
    
sol = Solution()
print(sol.reverse(1534236469))