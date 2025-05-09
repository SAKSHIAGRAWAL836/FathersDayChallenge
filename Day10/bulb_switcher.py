# LeetCode: https://leetcode.com/problems/bulb-switcher/
# Date: 2025-05-09
# Approach: A bulb ends up ON only if it is toggled an odd number of times, which happens only for perfect square positions (like 1, 4, 9...) because they have an odd number of divisors.

def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))
