'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b))
        a = a.zfill(l)
        b = b.zfill(l)
        a = "0b" + a 
        b = "0b" + b 
        s = int(a, 2) + int(b, 2)
        return bin(s).replace("0b","")

sol = Solution()
print(sol.addBinary(a = "11", b = "1"))


