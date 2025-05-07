# LeetCode: https://leetcode.com/problems/excel-sheet-column-number/
# Date: 2025-05-08
# Approach: Use two pointers to separate odd and even indexed nodes, Track the heads of both sub-lists, Reconnect the odd list to the even list.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in map(ord, columnTitle):
            ans = ans * 26 + c - ord("A") + 1
        return ans
        
