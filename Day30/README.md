# Day 30 - LeetCode Solutions

## Problems Solved:
1. **[287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)**
2. **[543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)**

---

## 🧩 1. Find the Duplicate Number

### Problem:
You are given an array of `n + 1` integers where each integer is between `1` and `n` (inclusive). There is only one repeated number. You must find it without modifying the array and using only constant extra space.

### Approach:
We use **Floyd’s Tortoise and Hare (Cycle Detection)** algorithm:

1. **Phase 1** – Detect the cycle:
   - Use two pointers (`slow` and `fast`) to find the intersection point.
2. **Phase 2** – Find the entrance to the cycle (which is the duplicate number).

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Entrance of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

Time Complexity: O(n)
Space Complexity: O(1)

## 🌲 2. Diameter of Binary Tree

## Problem:
Find the diameter (longest path between any two nodes) of a binary tree. This path may or may not pass through the root.

## Approach:
Use post-order DFS traversal to compute:

The depth of left and right subtrees.

Update the maximum diameter at each node as left_depth + right_depth.
```
python
Copy
Edit
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def maxDepth(root):
            nonlocal ans
            if not root:
                return 0
            l = maxDepth(root.left)
            r = maxDepth(root.right)
            ans = max(ans, l + r)
            return 1 + max(l, r)
        
        maxDepth(root)
        return ans
```

Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree.


✅ Status:
Both problems passed all test cases successfully with optimal time and space usage.

Happy coding! 🎯 
