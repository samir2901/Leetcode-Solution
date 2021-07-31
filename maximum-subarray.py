'''
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
'''

class Solution:
    def maxSubArray(self, nums):
        l = len(nums)
        sL = [None for i in range(l)]
        sL[0] = nums[0]
        maxS = nums[0]
        for i in range(1,l):
            sL[i] = max(sL[i-1]+nums[i],nums[i])
            maxS = max(sL[i],maxS)
        return maxS
       
                
         
        

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
        