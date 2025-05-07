# LeetCode: https://leetcode.com/problems/odd-even-linked-list/
# Date: 2025-05-08
# Approach: Use two pointers to separate odd and even indexed nodes, Track the heads of both sub-lists, Reconnect the odd list to the even list.

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        a = head
        b = c = head.next
        while b and b.next:
            a.next = b.next
            a = a.next
            b.next = a.next
            b = b.next
        a.next = c
        return head
        
