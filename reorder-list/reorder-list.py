# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        解题思路：
        1. 寻找中间点
        2. 后半部分reverse
        3. 合并
        """
        if not head:
            return
        
        mid = self.getMiddle(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.listReverse(l2)
        self.listMerge(l1, l2)
    
    def getMiddle(self, head: ListNode) -> ListNode:
        x = y = head
        while y.next and y.next.next:
            x = x.next
            y = y.next.next
        return x
    
    def listReverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            aftr = curr.next
            curr.next = prev
            prev = curr
            curr = aftr
        return prev

    def listMerge(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp
        
        