class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        brute force
        iterate the whole array and get the min value,
        and the min value is the one we return
        time: O(n) space: O(1)
        """
        return min(nums)