# Leetcode: https://leetcode.com/problems/binary-tree-right-side-view/description/
# Date: 2025-06-01
# Approach: Solved using level-order traversal (BFS) to collect the rightmost node of each level—great practice for binary tree problems

def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                root = q.popleft()
                if i == size - 1:
                    ans.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)

        return ans
