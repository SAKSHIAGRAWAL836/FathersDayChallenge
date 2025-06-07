# Leetcode: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
# Date: 2025-06-07

stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
