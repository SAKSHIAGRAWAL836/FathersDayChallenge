# 🚀 LeetCode Grind: Day 21

## ✅ Problems Solved:

1. **[678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) — Medium**
2. **[119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/) — Easy**

---

## 🧠 Problem 1: Valid Parenthesis String

### 🔗 Link:
[LeetCode 678](https://leetcode.com/problems/valid-parenthesis-string/)

### 📝 Approach:
Used a **Greedy + Range Tracking** method:
- Keep track of the **minimum (`low`) and maximum (`high`) possible open brackets** at each step.
- Handle `*` as:
  - `'('` → increase both `low` and `high`
  - `')'` → decrease both `low` and `high`
  - `'*'` → adjust `low--` (if possible) and `high++`
- If `high` drops below 0, return `false` (too many closing brackets).
- If `low == 0` at the end, return `true`.

### 🧪 Example:
Input: `"(*)"`  
Output: `true`

### ⌛ Time Complexity:
`O(n)` — single pass over the string.

---

## 🧠 Problem 2: Pascal's Triangle II

### 🔗 Link:
[LeetCode 119](https://leetcode.com/problems/pascals-triangle-ii/)

### 📝 Approach:
Used **Dynamic Programming with in-place updates**:
- Initialize an array of length `rowIndex + 1`.
- Iterate from `i = 2` to `rowIndex`.
- Update from right to left to avoid overwriting needed values.

### 🧪 Example:
Input: `rowIndex = 3`  
Output: `[1, 3, 3, 1]`

### ⌛ Time Complexity:
`O(rowIndex²)` — due to nested loop  
### 📦 Space Complexity:
`O(rowIndex)` — optimized from 2D to 1D array

---

## 🔄 Summary

| Problem | Approach | Time Complexity | Space Complexity |
|--------|----------|-----------------|------------------|
| Valid Parenthesis String | Greedy, range bounds | O(n) | O(1) |
| Pascal's Triangle II | In-place DP | O(n²) | O(n) |

---

📅 **Day 21 completed** with both problems ✅  
Let’s keep the streak going! 🔥

