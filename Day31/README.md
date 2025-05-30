## 🔁 832. Flipping an Image — Easy
## Problem: Given an n x n binary matrix, flip the image horizontally (reverse each row), then invert the bits.

## Approach:

Loop through each row.

Reverse it using slicing or a reverse loop.

Invert each bit (0 ➝ 1, 1 ➝ 0).

Store the new row in the result.

```python
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(image)):
            ans = []
            for j in range(len(image) - 1, -1, -1):
                ans.append(1 if image[i][j] == 0 else 0)
            res.append(ans)
        return res
```
## 🌳 104. Maximum Depth of Binary Tree — Easy
## Problem: Find the maximum depth of a binary tree — the number of nodes along the longest path from root to leaf.

## Approach:

Use recursion to check the depth of left and right subtrees.

Base case: if root is None, return 0.

Recursively return 1 + max(left_depth, right_depth).

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```
