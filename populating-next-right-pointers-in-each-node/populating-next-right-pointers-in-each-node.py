"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        null = '#'
        
        if not root:
            return root
        
        pre = root
        while pre.left:
            tmp = pre
            while tmp:
                tmp.left.next = tmp.right
                if tmp.next:
                    tmp.right.next = tmp.next.left
                tmp = tmp.next
            pre = pre.left
            
        return root