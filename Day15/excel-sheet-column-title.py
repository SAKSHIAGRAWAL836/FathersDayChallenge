# LeetCode: https://leetcode.com/problems/excel-sheet-column-title/description/
# Date: 2025-05-14

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber:
            columnNumber -= 1
            ans += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26
        return ans[::-1]


columnNumber = 28
print(Solution().convertToTitle(columnNumber))
