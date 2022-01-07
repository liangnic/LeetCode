# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        head, ans = self.head, self.head
        i, j = 1, 1
        
        while head.next:
            i += 1
            head = head.next
            if random.random() < j/i :
                ans = ans.next
                j += 1
        
        return ans.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()