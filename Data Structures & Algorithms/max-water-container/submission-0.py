class Solution:
    def maxArea(self, heights: List[int]) -> int:
       # the size of a container can store is:
       # min(left, right) * (right - left + 1)
       # Brute Force: 
       # we need to find all the combination left and right
       # and find their size, and then find the max size
       # Two pointer:
       # find the current size
       # if move the shorter one inward
        left = 0
        right = len(heights) - 1
        max_size = 0
        while left < right:
            current_size = min(heights[left], heights[right]) * (right - left)
            # print(current_size, left, heights[left], right, heights[right] )
            max_size = max(current_size, max_size)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_size
    