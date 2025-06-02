🚀 Day 34 - LeetCode Daily Progress
✅ Problems Solved:
1. 58. Length of Last Word
Difficulty: Easy

Topic: String

🧠 Approach:
Start from the end of the string and skip trailing spaces.

Use a pointer (i) to find the last non-space character.

Mark this as the end of the last word (lastIndex).

Continue traversing backward until a space is found.

The difference between lastIndex and i gives the length of the last word.

✅ Code Strategy:
Efficient O(n) solution with O(1) space.

Avoids built-in functions like split().

2. 114. Flatten Binary Tree to Linked List
Difficulty: Medium

Topic: Binary Tree / Linked List

🧠 Approach:
Use post-order traversal to flatten left and right subtrees first.

Store references to the left and right subtrees.

Make the left subtree the right subtree.

Then, append the original right subtree to the end of this new right subtree.

Set root.left = None as per the linked list requirement.

✅ Code Strategy:
Recursive DFS.

Uses an in-place technique with no extra space beyond the recursion stack.

