# Leetcode: https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# Date: 2025-06-05
# Approach:

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s: str) -> bool:
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        return next((word for word in words if isPalindrome(word)), '')
