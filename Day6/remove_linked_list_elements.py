# LeetCode: https://leetcode.com/problems/remove-linked-list-elements/
# Date: 2025-05-06
''' Approach: Create a dummy node pointing to the head to handle edge cases (like deleting head).
  - Traverse the list and remove nodes whose value equals the target.
  - Reconnect the previous node to skip the matched node.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy

        while head :
            if head.val != val:
                prev.next = head
                prev = prev.next
            head =  head.next
        prev.next = None

        return dummy.next
        
