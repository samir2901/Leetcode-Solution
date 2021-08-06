'''
Given a string s consists of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        l = s.split(" ")
        return len(l[len(l)-1])

sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))