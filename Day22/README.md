# 📅 LeetCode Journey — Day 22

Today I tackled two problems: one on string manipulation using a stack and another classic majority vote problem. Steady progress!

---

## ✅ Problems Solved

### 1. [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) — `Medium`

**Concepts:** Stack, String  
**Approach:**  
- First pass: Use a stack to track unmatched `(` and mark indices of invalid `)`.
- Second pass: Build a valid string by skipping all invalid indices.

**What I learned:**  
- Balancing parentheses efficiently with a stack.
- Two-pass cleanup is a handy technique for string problems.

---

### 2. [169. Majority Element](https://leetcode.com/problems/majority-element/) — `Easy`

**Concepts:** Boyer-Moore Voting Algorithm  
**Approach:**  
- Maintain a `count` and a `candidate`.
- If the count hits 0, change the candidate.
- Works since a majority element appears more than ⌊n / 2⌋ times.

**What I learned:**  
- Elegant O(n) time, O(1) space solution.
- Boyer-Moore is a must-know for interviews.

---

## 📊 Progress

| Metric                 | Value   |
|------------------------|---------|
| Problems Solved Today  | 2       |
| Total Days Completed   | 22      |
| Streak                 | ✅ Going strong! |

---

## 🔜 Up Next

- Tree and Graph problems incoming 🌲📈  
- Will revisit Dynamic Programming soon for a challenge! 💥
