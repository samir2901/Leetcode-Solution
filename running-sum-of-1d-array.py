'''Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]'''

class Solution:
    def runningSum(self, nums):
        x = []
        s = 0
        for i in range(0, len(nums)):
            s = s + nums[i]
            x.append(s)
        return x
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.runningSum([1,1,1,1,1]))

            
