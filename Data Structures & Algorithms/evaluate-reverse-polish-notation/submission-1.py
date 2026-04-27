class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        stack = [] 

        def is_num(s: str) -> bool:
            try:
                int(s)
            except ValueError:
                return False
            return True

        while tokens:
            cur = tokens.pop(0)
            if is_num(cur):
                stack.append(int(cur))
            else:
                prev2 = stack.pop()
                prev1 = stack.pop()
                if cur == "+":
                    cur = prev1 + prev2
                elif cur == "-":
                    cur = prev1 - prev2
                elif cur == "*":
                    cur = prev1 * prev2
                elif cur == "/":
                    cur = prev1 / prev2
                stack.append(int(cur))
        return stack[0]