# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        currNode = head
        
        d = {}
        while currNode:
            if currNode not in d:
                d[currNode] = 1
                currNode = currNode.next
            else:
                return True
        
        return False