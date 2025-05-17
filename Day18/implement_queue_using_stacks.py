# Leetcode: https://leetcode.com/problems/implement-queue-using-stacks/description/
# Date: 2025-05-17
# Approach: Solidified understanding of data structure transformations.

def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)


    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
         return not self.stack1 and not self.stack2
