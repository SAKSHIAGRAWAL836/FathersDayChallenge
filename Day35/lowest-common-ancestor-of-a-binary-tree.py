# Leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Date: 2025-06
# Approach: 

if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
