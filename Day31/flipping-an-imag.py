# Leetcode: https://leetcode.com/problems/flipping-an-image/description/
# Date: 2025-05-30
# Approach: Flipped each row in a binary matrix horizontally. Then inverted each bit (0 ➝ 1 and 1 ➝ 0).

def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(0, len(image)):
            ans = []
            for j in range(len(image)-1, -1, -1):
                if image[i][j] == 0:
                    ans.append(1)
                else:
                    ans.append(0)
            res.append(ans)

        return res
