# Leetcode: https://leetcode.com/problems/contains-duplicate/description/
# Date: 2025-05-17
# Approach:Leveraged Python's set() to detect duplicates in linear time.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
        
