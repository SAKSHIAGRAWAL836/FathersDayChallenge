# Leetcode: 
# Date: 2025-05-16
# Approach:  Used a hash map to check for the complement of each element in a single pass for constant time lookup

def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            if (y := target - x) in d:
                return [d[y], i]
            d[x] = i
