# Leetcode: https://leetcode.com/problems/lexicographically-smallest-palindrome/description/
# Date: 2025-06-01
# Approach: A string manipulation problem where I turned a given string into the smallest possible palindrome in terms of lexicographic order with the minimum number of changes.

def makeSmallestPalindrome(self, s: str) -> str:
        chars = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            minChar = min(chars[i], chars[j])
            chars[i] = minChar
            chars[j] = minChar
            i += 1
            j -= 1

        return ''.join(chars)
