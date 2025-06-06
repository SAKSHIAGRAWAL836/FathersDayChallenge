🌱 Day 35 of #100DaysOfCode
Today was a mix of tree traversal and string processing—both simple in appearance, but packed with useful concepts. Here's what I worked on:

✅ Problem 1: Lowest Common Ancestor of a Binary Tree
📌 Leetcode 236 | 🔗 Medium
🧠 Concepts Used: Recursion, Binary Tree traversal
🛠️ Logic:

If either node p or q is found at the current root, return the root.

Recurse left and right.

If both sides return non-null, current root is the LCA.

Else, return whichever side is non-null.

python
Copy
Edit
def lowestCommonAncestor(self, root, p, q):
    if not root or root == p or root == q:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left or right
🔍 Takeaway: Classic recursion problem. A must-know for binary trees!

✅ Problem 2: Number of Segments in a String
📌 Leetcode 434 | 🔗 Easy
🧠 Concepts Used: String manipulation, Built-in Python functions
🛠️ Logic:

Use split() to break the string by spaces.

Return the length of the resulting list.

python
Copy
Edit
def countSegments(self, s: str) -> int:
    return len(s.split())
🔍 Takeaway: Don’t overthink easy problems—sometimes Python one-liners do the job perfectly.

📅 Progress Summary:
Two more problems down. Trees are growing on me 🌳, and Python continues to be a joy to code in.
