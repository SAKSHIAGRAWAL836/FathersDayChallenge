✅ Problem 1: 633. Sum of Square Numbers
Link: https://leetcode.com/problems/sum-of-square-numbers/
Level: Medium
Topic: Two Pointers, Math

🧠 Problem Statement:
Given a non-negative integer c, determine whether there are two integers a and b such that:
a² + b² = c

💡 Approach:
Use two pointers: left = 0 and right = sqrt(c)
While left <= right, calculate left² + right² and compare with c
If the sum is less, move left ahead; if more, move right back.
🧪 Sample Test:
Input: c = 5
Output: True
Explanation: 1² + 2² = 1 + 4 = 5

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            sum_of_squares = left * left + right * right
            if sum_of_squares == c:
                return True
            elif sum_of_squares < c:
                left += 1
            else:
                right -= 1
        return False
        
