# LeetCode : https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
# Date : 2025-05-08
# Approach : Used a two-pointer approach to swap the k-th node from the start and end. Loved the precision this problem demanded!

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(k - 1):
            fast = fast.next
        p = fast
        while fast.next:
            fast, slow = fast.next, slow.next
        q = slow
        p.val, q.val = q.val, p.val
        return head
