# Leetcode: https://leetcode.com/problems/partition-list/description/
# Date: 2025-05-13
# Approach:We create two linked lists l and r, one to store nodes less than x and the other to store nodes greater than or equal to x. Then we concatenate them.

def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l = ListNode()
        r = ListNode()
        tl, tr = l, r
        while head:
            if head.val < x:
                tl.next = head
                tl = tl.next
            else:
                tr.next = head
                tr = tr.next
            head = head.next
        tr.next = None
        tl.next = r.next
        return l.next
