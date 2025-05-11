# Leetcode: 
# Date: 2025-05-11

def countOdds(self, low: int, high: int) -> int:
        return ((high + 1) >> 1) - (low >> 1)
