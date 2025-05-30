# Leetcode: https://leetcode.com/problems/find-the-duplicate-number/description/
# Date: 2025-05-29
# Approach: Used Floyd’s Tortoise and Hare cycle detection algorithm 🐢🐇

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find the intersection point of the two pointers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the entrance of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
