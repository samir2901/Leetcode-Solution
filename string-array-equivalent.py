'''
Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
'''

class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        str1 = ''
        for e in word1:
            str1+=e
        str2 = ''
        for e in word2:
            str2+=e
        return str1==str2

sol = Solution()        
print(sol.arrayStringsAreEqual(["ab", "c"],["a", "bc"]))