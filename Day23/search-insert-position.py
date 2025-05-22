# Leetcode: https://leetcode.com/problems/search-insert-position/description/
# Date: 2025-05-22
# Approach: This function finds the index where a given target should be inserted in a sorted array nums, such that the array remains sorted. If the target is found, it returns its index. If not, it returns the index where it can be inserted.



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
