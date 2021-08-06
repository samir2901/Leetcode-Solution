'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
    cs = []
    def climbStairs(self, n: int) -> int:
        self.cs = [-1 for i in range(n+1)]
        return self.function(n)
        
    def function(self, i):
        if i == 1:
            self.cs[1] = 1
        elif i == 2:
            self.cs[2] = 2 
        else:           
            if self.cs[i] == -1:
                self.cs[i] = self.function(i - 1) + self.function(i - 2)
        return self.cs[i]
        

sol = Solution()
print(sol.climbStairs(38))
        