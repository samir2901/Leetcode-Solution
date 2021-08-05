'''
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]
'''

class Solution:
    def generate(self, numRows: int):
        l = []        
        for i in range(0,numRows):
            m = []
            for j in range(0,i+1):
                if i==j or j==0:
                    x = 1
                else:
                    x = l[i-1][j-1] + l[i-1][j]                
                m.append(x)
            l.append(m)
        return l
            

sol = Solution()
print(sol.generate(5))