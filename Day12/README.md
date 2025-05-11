# 🚀 LeetCode Solutions – May 11, 2025
#DAY 12

This repository contains clean Python solutions with explanations for selected LeetCode problems solved on **May 11, 2025**.

---

## 🧩 Problem 1: Insert Greatest Common Divisors in Linked List

**Problem Link:** [LeetCode #2807](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/)  
**Approach:**  
Traverse the linked list and insert a new node with the GCD of each adjacent node's values.

**One-liner Logic:**  
> While traversing, insert `ListNode(gcd(curr.val, curr.next.val))` between each pair of nodes.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

---

## 🧠 Problem 2: Count Odd Numbers in an Interval Range

**Problem Link:** [LeetCode #1523](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)  
**Approach:**  
Use math to calculate the number of odd numbers in the range without looping.

**One-liner Logic:**  
> Return `(high - low) // 2 + (1 if low % 2 != 0 or high % 2 != 0 else 0)`

**Time Complexity:** `O(1)`  
**Space Complexity:** `O(1)`

---

## 📂 Folder Structure

