# Leetcode: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
# Date: 2025-05-11
# Approach: While traversing, insert ListNode(gcd(curr.val, curr.next.val)) between each pair of nodes.


def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = head, head.next
        while cur:
            x = gcd(pre.val, cur.val)
            pre.next = ListNode(x, cur)
            pre, cur = cur, cur.next
        return head
        
