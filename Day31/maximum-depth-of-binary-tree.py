# Leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Date : 2025-05-30
# Approach: Used recursive DFS to find the longest path from root to leaf.
#• Strengthened my understanding of recursion in binary trees.

def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
