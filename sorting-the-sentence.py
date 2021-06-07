'''
Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
Example 2:

Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
'''

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')
        sentence = [None for i in range(len(words))]
        for w in words:
            index = self.getWordIndex(w)            
            word = w[0:len(w)-1]
            sentence[index] = word
        return ' '.join(sentence)
        

    def getWordIndex(self,word):
        return int(word[len(word)-1])-1
        

sol = Solution()
print(sol.sortSentence("Myself2 Me1 I4 and3"))