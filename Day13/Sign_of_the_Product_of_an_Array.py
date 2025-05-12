# Leetcode: https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
# Date: 2025-05-12
# Approach: Count the number of negative numbers and check for zero to determine the sign of the product without calculating it.

def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for v in nums:
            if v == 0:
                return 0
            if v < 0:
                ans *= -1
        return ans
