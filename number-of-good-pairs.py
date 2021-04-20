'''
Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
'''

class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    count+=1
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.numIdenticalPairs([1,2,3]))
        