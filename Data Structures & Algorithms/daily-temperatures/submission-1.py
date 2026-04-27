class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        time: O(n)
        space: O(n)
        """
        res = [0] * len(temperatures)
        stack = []

        for idx, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                prev_num, prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx
            stack.append((num, idx))

        return res
