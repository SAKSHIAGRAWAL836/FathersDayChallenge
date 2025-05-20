
---

### ✅ `119.Pascals_Triangle_II.md`

```markdown
# 🧩 Problem: 119. Pascal's Triangle II

### 🔗 Link:
[https://leetcode.com/problems/pascals-triangle-ii/](https://leetcode.com/problems/pascals-triangle-ii/)

### ✅ Status: Solved

---

## 🧠 Approach:

Optimized using **1D Dynamic Programming**:
- Use an array `res` of size `rowIndex + 1`
- Start with `res[0] = 1`
- For each row from 1 to `rowIndex`, update values from right to left:
  ```python
  for i in range(1, rowIndex+1):
      for j in range(i, 0, -1):
          res[j] += res[j - 1]
