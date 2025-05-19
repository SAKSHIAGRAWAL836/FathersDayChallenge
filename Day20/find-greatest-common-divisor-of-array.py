# Leetcode: https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
# Date: 2025-05-19
# Approach: 

def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums), min(nums))
