# LeetCode: https://leetcode.com/problems/happy-number/
# Date: 2025-05-06
# Approach: Use a set to detect cycles

def isHappy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(c)**2 for c in str(n))
    return n == 1
