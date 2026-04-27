class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Use a stack
        always keep the stack monotonical increasing (or equal?)
        and pop out larger items when new bar join in
        and compute the size
        time: O(n)
        space: O(n)
        """

        stack = []
        max_size = 0
        heights.append(0)
        for i, height in enumerate(heights):
            print((height, i))
            start_idx = i
            while stack and stack[-1][0] > height:
                prev_height, prev_idx = stack.pop()
                print("pop ", prev_height, prev_idx)
                max_size = max(prev_height * (i - prev_idx), max_size)
                print("max_size", max_size)
                start_idx = prev_idx
            stack.append((height, start_idx))
            print("add", (height, i))

        # while stack:
        #     prev_height, prev_idx = stack.pop()
        #     max_size = max(prev_height * (len(heights) - prev_idx), max_size)

        return max_size
            
        