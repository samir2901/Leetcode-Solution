'''
Example 1:

Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
Example 2:

Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
'''

class Solution:
    def countNumber(self, index, items, ruleValue):
        count = 0
        for i in range(len(items)):
            if ruleValue == items[i][index]:
                count+=1
        return count

    def countMatches(self, items, ruleKey, ruleValue):
        if ruleKey == "type":
            #index = 0
            count = self.countNumber(0,items,ruleValue)            
        elif ruleKey == "color":
            #index = 1
            count = self.countNumber(1,items,ruleValue)            
        elif ruleKey == "name":
            #index = 2
            count = self.countNumber(2,items,ruleValue)            
        return count
        
sol = Solution()
print(sol.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color","silver"))