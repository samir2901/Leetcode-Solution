'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==0:
            return ""
        prefix = strs[0]
        for i in range(1,len(strs)):
            prefix = self.commonPrefix(prefix,strs[i])
        return prefix

    def commonPrefix(self, str1, str2):
        prefix = ""
        i = 0
        j = 0
        while i<len(str1) and j<len(str2):
            if str1[i] == str2[j]:
                prefix+=str1[i]
            else:
                break            
            i+=1
            j+=1
        return prefix

     
        

sol = Solution()
#print(sol.commonPrefix("fower","flr"))
print(sol.longestCommonPrefix(["cir","car"]))
        