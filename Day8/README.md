# Day 8 - Dr. G Viswanathan 50 Days Coding Challenge

## 📘 Problems

1. **Math Based**: [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)
2. **DSA Based**: [Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

---

## 📌 Problem 1: Excel Sheet Column Number

**Approach**:  
This problem is based on converting a string representing an Excel column title (like "A", "AB") into its corresponding column number using base-26 logic.  
Loop through each character, convert it to a number using `ord()`, and accumulate the result.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

---

## 📌 Problem 2: Odd Even Linked List

**Approach**:  
We separate the list into odd and even nodes using two pointers (`a` for odd, `b` for even), then reconnect them. This preserves relative order and solves the problem in-place.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

---
