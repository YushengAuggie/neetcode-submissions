from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        r = 0

        while r < len(nums):
            # largest to the head
            # pop out smaller numbers
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            # move out of window elements from top
            while dq and dq[0] <= r - k:
                dq.popleft()
            if r + 1 >= k:
                res.append(nums[dq[0]])
            r += 1
        return res



            


            
       