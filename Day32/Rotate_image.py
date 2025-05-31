#Leetcode: https://leetcode.com/problems/rotate-image/description/
# Date: 2025-05-31
# Approach: Reversed the matrix and transposed it - Achieved in-place 90-degree rotation

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i, j in itertools.combinations(range(len(matrix)), 2):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
