# 🧩 Problem: 678. Valid Parenthesis String

### 🔗 Link:
[https://leetcode.com/problems/valid-parenthesis-string/](https://leetcode.com/problems/valid-parenthesis-string/)

### ✅ Status: Solved

---

## 🧠 Approach:

Used a **Greedy technique** to track the possible range of open parentheses:

- `low`: minimum possible number of open brackets
- `high`: maximum possible number of open brackets
- When encountering:
  - `'('` → `low++`, `high++`
  - `')'` → `low--`, `high--`
  - `'*'` → `low--`, `high++` (could be `(`, `)` or empty)
- If `high < 0`, it's invalid (too many closing brackets).
- If `low < 0`, reset it to 0 because we can't have negative open brackets.

---

## 🧪 Example:

```text
Input:  "()"
Output: true

Input:  "(*)"
Output: true

Input:  "(*))"
Output: true
