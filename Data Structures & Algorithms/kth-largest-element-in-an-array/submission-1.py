import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        time: O(nlogn)
        space: O(n)
        """
        heapq.heapify(nums)
        res = heapq.nlargest(k, nums)
        return res[-1]

            
        