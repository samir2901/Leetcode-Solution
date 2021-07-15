'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        openBr = ["(","[","{"]
        closedBr = [")","]","}"]

        if len(s) == 0 or len(s) == 1:
            return False
        
        for char in s:
            if char in openBr:
                stack.append(char)
            elif char in closedBr:
                if len(stack)!=0:
                    br = stack.pop()
                    if self.validPair(br,char):
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True 
        return False

    def validPair(self, p1, p2):
        if p1 == '(' and p2 == ')':
            return True
        elif p1 == '[' and p2 == ']':
            return True
        elif p1 == '{' and p2 == '}':
            return True
        return False

sol = Solution()
print(sol.isValid(')('))