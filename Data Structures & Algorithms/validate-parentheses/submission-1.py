
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
             ")": "(",
             "}": "{",
             "]": "[",
        }

        queue = deque()
        for c in s:
            if c not in pairs:
                queue.append(c)
            else:
                if len(queue) and queue[-1] == pairs[c]:
                    queue.pop()
                else:
                    return False
        return len(queue) == 0
