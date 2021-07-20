'''
Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val 
        self.next = next 

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head       

        while l1 and l2:            
            if l1.val <= l2.val:
                new_node = ListNode(val=l1.val)                    
                l1 = l1.next
            else:
                new_node = ListNode(val=l2.val)
                l2 = l2.next
            current.next = new_node
            current = new_node            
        

        while l1:
            new_node = ListNode(val=l1.val)
            current.next = new_node
            current = new_node 
            l1 = l1.next
        
        while l2:
            new_node = ListNode(val=l2.val)
            current.next = new_node
            current = new_node 
            l2 = l2.next

        head = head.next
        return head