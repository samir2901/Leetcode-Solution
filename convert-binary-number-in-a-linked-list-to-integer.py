class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None
    
def getDecimalValue(head: ListNode) -> int:
    value = 0
    while head:
        value = 2 * value + head.value
        head = head.next
    return value
    



