# Leetcode: https://leetcode.com/problems/longest-valid-parentheses/description/
# Date: 2025-05-22
# Approach:
'''
We add a dummy ) at the beginning to simplify 0-based indexing and avoid extra boundary checks.
dp[i] stores the length of the longest valid parentheses ending at index i in s2.
The key condition checks:
-If current s2[i] == ')', and
-There is a '(' that matches it at position i - dp[i-1] - 1,
-Then add: 
    -dp[i-1]: valid length just before,
    -dp[prev_index - 1]: valid length before the matching (, 
    -2: for the matching pair.'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s2 = ')' + s
    # dp[i] := the length of the longest valid parentheses in the substring
    # s2[1..i]
        dp = [0] * len(s2)

        for i in range(1, len(s2)):
            if s2[i] == ')' and s2[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2

        return max(dp)
