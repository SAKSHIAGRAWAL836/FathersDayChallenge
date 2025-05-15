✅ Problem 2: 237. Delete Node in a Linked List
Link: https://leetcode.com/problems/delete-node-in-a-linked-list/
Level: Medium
Topic: Linked List

🧠 Problem Statement:
Given only access to a node in a singly linked list (not the head), delete it.

💡 Approach:
Copy the value of the next node into the current node
Then link the current node to next.next
This simulates deleting the current node without head reference.
🧪 Sample Test:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
