# Leetcode: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
# Date: 2025-06-02
# Approach:

 if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left  # flattened left
        right = root.right  # flattened right

        root.left = None
        root.right = left

    # Connect the original right subtree to the end of the new right subtree.
        rightmost = root
        while rightmost.right:
            rightmost = rightmost.right
        rightmost.right = right
