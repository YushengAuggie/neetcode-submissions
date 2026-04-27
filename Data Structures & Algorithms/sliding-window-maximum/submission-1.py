import heapq
from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        heap -> get max
        save a dict for characters in the window
        and every time we see the max is not in the window, we just pop out
        till the max is in the window
        Time: O(nlogn)
        Space: O(n)
        """
        hp = []
        res = []
        window = defaultdict(int)
        for i, num in enumerate(nums):
            #print(hp)
            #print(window)
            heapq.heappush(hp, -num)
            window[num] += 1
            if i >= k:
                window[nums[i - k]] -= 1
            while hp and window[-hp[0]] == 0:
                #print("pop",hp[0])
                heapq.heappop(hp)

            if len(hp) >= k:
                #print("append ", -hp[0])
                res.append(-hp[0])


            #print()
        return res

            
