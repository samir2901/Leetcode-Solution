'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
'''

class Solution:
    def isPalindrome(self, s):
        l = s.split(" ")        
        s1 = "".join(l)
        for char in s1:
            if not char.isalnum():
                s1 = s1.replace(char,"")
        s1 = s1.lower()
        s2 = s1[::-1]
        return s1==s2

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))