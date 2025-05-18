# Leetcode: https://leetcode.com/problems/valid-parentheses/description/
# Date: 2025-05-18
# Approach: Use a stack to push expected closing brackets for each opening bracket, and pop to match each closing bracket; if mismatched or stack isn’t empty at the end, return false.

def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(':stack.append(')')
            elif c == '{':stack.append('}')
            elif c == '[':stack.append(']')
            elif not stack or stack.pop() != c:
                return False

        return not stack
