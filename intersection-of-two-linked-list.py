'''
Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        if headA is None or headB is None:
            return None 
        lenA = self.listlen(headA)
        lenB = self.listlen(headB)
        d = abs(lenA - lenB)
        if lenA > lenB:
            c = 0
            while c < d:
                headA = headA.next
                c += 1
        elif lenA < lenB:
            c = 0
            while c < d:
                headB = headB.next
                c += 1
        t1 = headA
        t2 = headB
        while t1 is not None and t2 is not None:
            if t1 is t2:
                return t1 
            t1 = t1.next
            t2 = t2.next
        
    
    def listlen(self, head):
        if head is None:
            return 0
        else:
            c = 0
            t = head
            while t != None:
                c += 1
                t = t.next 
            return c



        