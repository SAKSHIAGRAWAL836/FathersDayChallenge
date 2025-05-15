# Day 16 - LeetCode Practice

Today’s problems focus on mathematical logic and linked list manipulation.

---

### ✅ Problem 1: 633. Sum of Square Numbers  
**Link:** https://leetcode.com/problems/sum-of-square-numbers/  
**Level:** Medium  
**Topic:** Two Pointers, Math

#### 🧠 Problem Statement:
Given a non-negative integer `c`, determine whether there are two integers `a` and `b` such that:  
a² + b² = c

#### 💡 Approach:
- Use two pointers: `left = 0` and `right = sqrt(c)`
- While `left <= right`, calculate `left² + right²` and compare with `c`
- If the sum is less, move `left` ahead; if more, move `right` back.

#### 🧪 Sample Test:
Input: c = 5  
Output: True  
Explanation: 1² + 2² = 1 + 4 = 5

---

### ✅ Problem 2: 237. Delete Node in a Linked List  
**Link:** https://leetcode.com/problems/delete-node-in-a-linked-list/  
**Level:** Medium  
**Topic:** Linked List

#### 🧠 Problem Statement:
Given only access to a node in a singly linked list (not the head), delete it.

#### 💡 Approach:
- Copy the value of the next node into the current node
- Then link the current node to `next.next`
- This simulates deleting the current node without head reference.

#### 🧪 Sample Test:
Input: head = [4,5,1,9], node = 5  
Output: [4,1,9]

---

📝 **Progress:**  
Another step ahead in mastering problem-solving with Python and understanding underlying data structures and algorithms.

📆 **Day 16 Completed!**
