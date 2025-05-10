# LeetCode: https://leetcode.com/problems/factorial-trailing-zeroes/description/
# Date: 2025-05-10
'''Approach: The problem is actually asking how many factors of 5 are there in [1,n].
Let's take 130 as an example for analysis:
Divide by 5 for the first time, get 26, indicating that there are 26 numbers containing the factor 5;
Divide by 5 for the second time, get 5, indicating that there are 5 numbers containing the factor 52;
Divide by 5 for the third time, get 1, indicating that there is 1 number containing the factor 53;
Sum up to get the count of all factors of 5 in [1,n].
The time complexity is O(log⁡n), and the space complexity is O(1).'''

ans = 0
        while n:
            n //= 5
            ans += n
        return ans
