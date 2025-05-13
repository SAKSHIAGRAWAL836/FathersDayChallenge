
# 📅 Day 14 - LeetCode Challenge

Today’s focus was on solving two medium-level problems that test core algorithmic concepts like digit manipulation and linked list partitioning.

---

## 🔁 Problem 1: Reverse Integer

- **LeetCode ID:** 7  
- **Category:** Math, Overflow Handling  
- **Link:** [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

### 🧠 Problem Statement

Given a signed 32-bit integer `x`, return its digits reversed. If reversing causes the result to go beyond the signed 32-bit integer range (`[-2^31, 2^31 - 1]`), return 0.

### 💡 Approach

1. Determine the sign of the input.
2. Extract digits one by one using modulo and division.
3. Construct the reversed number.
4. Check for overflow before returning the final result.

### ✅ Code Snippet (Python)
```python
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = -1 if x < 0 else 1
        x *= sign

        while x:
            ans = ans * 10 + x % 10
            x //= 10

        return 0 if ans < -2**31 or ans > 2**31 - 1 else sign * ans
```

### 🧪 Example

| Input | Output |
|-------|--------|
| 123   | 321    |
| -123  | -321   |
| 120   | 21     |

---

## 🔗 Problem 2: Partition List

- **LeetCode ID:** 86  
- **Category:** Linked List, Two Pointers  
- **Link:** [Partition List](https://leetcode.com/problems/partition-list/)

### 🧠 Problem Statement

Given a linked list and an integer `x`, partition it so that:
- All nodes with values **less than `x`** come **before** nodes with values **greater than or equal to `x`**.
- The original **relative order** of nodes in each partition must be preserved.

### 💡 Approach

1. Create two dummy nodes for two partitions (`< x` and `>= x`).
2. Traverse the list and place each node into the appropriate partition.
3. Combine both partitions and return the merged list.

### ✅ Code Snippet (Python)
```python
class Solution:
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
```

### 🧪 Example

| Input List         | x | Output List      |
|--------------------|---|------------------|
| [1,4,3,2,5,2]       | 3 | [1,2,2,4,3,5]     |
| [2,1]              | 2 | [1,2]             |

---

## 🧩 Summary

| Problem             | Status    | Time Complexity |
|---------------------|-----------|------------------|
| Reverse Integer     | ✅ Solved | O(log n)         |
| Partition List      | ✅ Solved | O(n)             |

---

🔚 **End of Day 14**  
Great progress today! Strengthened skills in number manipulation and linked list handling. 🔥
