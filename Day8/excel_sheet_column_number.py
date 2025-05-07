# LeetCode: https://leetcode.com/problems/excel-sheet-column-number/
# Date: 2025-05-08
# Approach: Treat the string like a base-26 number system.
     #Iterate through each character, use ASCII logic:
     #ans = ans * 26 + (ord(char) - ord('A') + 1)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for c in map(ord, columnTitle):
            ans = ans * 26 + c - ord("A") + 1
        return ans
        
