'''
Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false

Input sentence = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"
Output: false
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = set(sentence)
        s = sorted(s)
        s = ''.join(s)          
        if s == 'abcdefghijklmnopqrstuvwxyz':
            return True
        return False              

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))


        
        