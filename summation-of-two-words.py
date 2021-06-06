'''
Example 1:

Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.
Example 2:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.
Example 3:

Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation: 
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.
'''

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        self.d = {}
        alpha = 'a'
        for i in range(0,26):
            self.d[alpha] = i 
            alpha = chr(ord(alpha)+1)

        num1 = self.createNum(firstWord)
        num2 = self.createNum(secondWord)
        num3 = self.createNum(targetWord)

        return (num1+num2)==num3
    
    def createNum(self,word):
        num = ''
        for c in word:
            num += str(self.d[c])
        num = int(num)
        return num

sol = Solution()
print(sol.isSumEqual('aaa','a','aab'))