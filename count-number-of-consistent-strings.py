'''
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
'''

class Solution:
    def countConsistentStrings(self, allowed, words) -> int:
        count = 0        
        for word in words:
            if self.isPresent(allowed,word):                
                count+=1
        return count 
    
    def isPresent(self, allowed, word):
        flag = False
        for char in word:
            if char in allowed:
                flag = True 
            else:
                flag = False
                break
        return flag 
            
sol = Solution()
print(sol.countConsistentStrings("cad",["cc","acd","b","ba","bac","bad","ac","d"]))

        