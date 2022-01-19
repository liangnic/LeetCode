# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        try:
            slow = head
            fast = head.next
            
            while fast is not slow:
                slow = slow.next
                fast = fast.next.next
        except:
            return None
        
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next
        
        return head
        