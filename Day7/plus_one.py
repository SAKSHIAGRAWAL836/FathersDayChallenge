# LeetCode: https://leetcode.com/problems/plus-one/
# Date: 2025-05-07
# Approach: Traverse from end, handle carry

    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        return [1] + digits
