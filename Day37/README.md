## 💻 Day 37 - LeetCode Problems
## ✅ Problem 1: 103. Binary Tree Zigzag Level Order Traversal
**Category**: Medium
**Topic Tags**: Tree, Breadth-First Search, Binary Tree
**Description**:
Return the zigzag level order traversal of a binary tree’s node values (i.e., left to right, then right to left for the next level and alternate between).

Example:

```lua
Copy
Edit
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```
Python Code:

```python
Copy
Edit
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        ans = []
        dq = deque([root])
        isLeftToRight = True

        while dq:
            currLevel = []
            for _ in range(len(dq)):
                if isLeftToRight:
                    node = dq.popleft()
                    currLevel.append(node.val)
                    if node.left:
                        dq.append(node.left)
                    if node.right:
                        dq.append(node.right)
                else:
                    node = dq.pop()
                    currLevel.append(node.val)
                    if node.right:
                        dq.appendleft(node.right)
                    if node.left:
                        dq.appendleft(node.left)
            ans.append(currLevel)
            isLeftToRight = not isLeftToRight

        return ans
```
## ✅ Problem 2: 2108. Find First Palindromic String in the Array
**Category**: Easy
**Topic Tags**: Array, String
**Description**:
Given an array of strings, return the first palindromic string in the array. If there is none, return an empty string.

##Example:

```vbnet
Copy
Edit
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
```
## Python Code:

```python
class Solution:
    def firstPalindrome(self, words):
        def isPalindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        return next((word for word in words if isPalindrome(word)), '')
```
