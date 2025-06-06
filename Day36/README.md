# 🚀 Day 36 of #100DaysOfCode

## ✅ Today’s Progress:
Solved two LeetCode problems in Python.

---

## 🔹 Problem 1: Sum Root to Leaf Numbers  
**Leetcode 129** | **Medium**

📌 **Concepts**: Tree Traversal, DFS, Accumulated Path Sum

🧠 **Summary**:  
Each root-to-leaf path in a binary tree represents a number (by joining the node values). The goal is to return the sum of all such numbers.

✅ **Approach**:  
Used Depth-First Search (DFS) to traverse each path from root to leaf and maintain a running number by multiplying the path so far by 10 and adding the current value.

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, path):
            nonlocal ans
            if not root:
                return
            if not root.left and not root.right:
                ans += path * 10 + root.val
                return
            dfs(root.left, path * 10 + root.val)
            dfs(root.right, path * 10 + root.val)
        dfs(root, 0)
        return ans
```
🧪 Test Case:
Input: [1,2,3]
Output: 25
Explanation: 12 (from 1→2) + 13 (from 1→3) = 25

## 🔹 Problem 2: Reverse Vowels of a String
**Leetcode 345** | **Easy**

📌 **Concepts**: Two Pointers, String Manipulation

🧠 **Summary**:
Given a string, reverse only the vowels.

✅ **Approach**:
Used two pointers (start and end) to scan and swap vowels from both ends, skipping consonants.

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        VOWELS = 'aeiouAEIOU'
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and chars[l] not in VOWELS:
                l += 1
            while l < r and chars[r] not in VOWELS:
                r -= 1
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        return ''.join(chars)
```
🧪 Test Case:
Input: "IceCreAm"
Output: "AceCreIm"

## 📘 Learnings:
Refined recursive DFS logic with nonlocal variables.

Strengthened two-pointer strategy for string problems.

Reinforced attention to base cases and input handling.

🔄 Up Next:
On to Day 37 🚀

#Python #LeetCode #100DaysOfCode #DataStructures #Algorithms
