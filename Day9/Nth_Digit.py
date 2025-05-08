# LeetCode: https://leetcode.com/problems/nth-digit/description/
# Date: 2025-05-08
# Approach: Dived into a number sequence and pinpointed the nth digit using math and logic. A satisfying brain teaser!

class Solution:
    def findNthDigit(self, n: int) -> int:
        k, cnt = 1, 9
        while k * cnt < n:
            n -= k * cnt
            k += 1
            cnt *= 10
        num = 10 ** (k - 1) + (n - 1) // k
        idx = (n - 1) % k
        return int(str(num)[idx])
