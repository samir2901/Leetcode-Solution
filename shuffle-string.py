'''
Example 1:

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
Example 3:

Input: s = "aiohn", indices = [3,1,4,2,0]
Output: "nihao"
Example 4:

Input: s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
Output: "arigatou"
Example 5:

Input: s = "art", indices = [1,0,2]
Output: "rat"
'''

class Solution:
    def restoreString(self, s, indices):
        output  = ['' for i in range(len(s))]
        for i in range(len(indices)):
            output[indices[i]] = s[i]
        return ''.join(output)
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreString("codeleet",[4,5,6,7,0,2,1,3]))
