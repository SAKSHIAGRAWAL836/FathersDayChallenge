📅 LeetCode Challenge – Day 15 (May 15, 2025)
🔥 Problems Solved
1. Two Sum (Easy)
Problem Statement:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

Approach:
Utilized a hash map to store visited numbers and their indices. For each number, we check if its complement (i.e., target - current) exists in the map. This allows us to solve the problem in O(n) time with a single pass.

Concepts Used: Hashing, Single Pass Iteration, Dictionary Lookup.

2. Min Stack (Medium)
Problem Statement:
Design a stack that supports push, pop, top, and getMin operations in constant time.

Approach:
Each element is stored as a pair [value, current_min]. While pushing, we compare the current value with the minimum so far and store both. This allows getMin() to return in O(1) time.

Concepts Used: Stack Data Structure, Auxiliary Tracking of Minimum Element, Tuple Storage.

🧠 Key Learnings
Reinforced how hash maps can be used for constant-time lookups in problems like Two Sum.

Understood how to maintain additional metadata in stack problems to achieve optimal time complexity for complex operations.

Practiced writing clean and optimized Python code with good time and space trade-offs.

📊 Stats
🧩 Total Problems Solved Today: 2

⏱ Time Complexity Achieved:

Two Sum: O(n)

Min Stack: O(1) for all operations

✅ What’s Next?
Continue with stack-based problems to strengthen understanding of space-efficient data structures.

Practice variations of hash-based solutions for pattern recognition in problem-solving.
