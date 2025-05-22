🚀 LeetCode Grind: Day 23  
✅ Problems Solved:  
32. Longest Valid Parentheses — Hard  
35. Search Insert Position — Easy  

🧠 Problem 1: Longest Valid Parentheses  
🔗 Link: [LeetCode 32](https://leetcode.com/problems/longest-valid-parentheses)

📝 Approach:  
Used Dynamic Programming with a modified string:
- Prepend ')' to the string to simplify index handling.
- Use a `dp` array where `dp[i]` represents the length of the longest valid substring ending at `i`.
- If `s[i] == ')'` and matching '(' is found at the right offset, update:
  `dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2`

🧪 Example:  
Input: `"(()())"`  
Output: `6`  

⌛ Time Complexity: O(n)  
📦 Space Complexity: O(n)  

🧠 Problem 2: Search Insert Position  
🔗 Link: [LeetCode 35](https://leetcode.com/problems/search-insert-position)

📝 Approach:  
Used Binary Search with left-closed, right-open interval:
- If `nums[mid] >= target`: move `right = mid`
- Else: move `left = mid + 1`
- Final answer is `left` — the correct insert position.

🧪 Example:  
Input: `nums = [1, 3, 5, 6], target = 2`  
Output: `1`  

⌛ Time Complexity: O(log n)  
📦 Space Complexity: O(1)  

🔄 Summary  
Problem | Approach | Time Complexity | Space Complexity  
--------|----------|-----------------|-----------------  
Longest Valid Parentheses | Dynamic Programming | O(n) | O(n)  
Search Insert Position | Binary Search | O(log n) | O(1)  

📅 Day 23 completed! Let’s keep the streak alive! 🔥
