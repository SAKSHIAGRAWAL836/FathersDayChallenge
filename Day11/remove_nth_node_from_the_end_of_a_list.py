# LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Date: 2025-05-10
''' Approach: We define two pointers fast and slow, both initially pointing to the dummy head node of the linked list.
Next, the fast pointer moves forward n steps first, then fast and slow pointers move forward together until the fast pointer reaches the end of the linked list. At this point, the node pointed to by slow.next is the predecessor of the 
n-th node from the end, and we can delete it.
The time complexity is O(n), where n is the length of the linked list. The space complexity is O(1).'''

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next
