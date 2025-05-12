# LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
# Date: 2025-05-12
# Approach: Use a dummy node and two pointers to skip over duplicate nodes and retain only unique values in the sorted linked list.

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(next=head)
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next
