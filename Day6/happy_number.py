# LeetCode: https://leetcode.com/problems/happy-number/
# Date: 2025-05-06
# Approach:  - A number is happy if the process of replacing the number by the sum of the squares of its digits eventually leads to 1.
 # - Use a set to store previously seen numbers to detect loops.
 #- Keep applying the transformation until the number becomes 1 or enters a loop.

class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()
        while n != 1 and n not in vis:
            vis.add(n)
            x = 0
            while n:
                n, v = divmod(n, 10)
                x += v * v
            n = x
        return n == 1
