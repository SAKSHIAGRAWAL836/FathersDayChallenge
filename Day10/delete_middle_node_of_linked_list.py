# LeetCode: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
# Date: 2025-05-09
# Approach: Use two pointers (slow and fast) to find the middle node, then delete it by updating the previous node’s next pointer.

def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node.
        slow.next = slow.next.next
        return dummy.next
