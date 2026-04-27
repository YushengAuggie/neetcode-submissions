class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        max_val = min_val = 1
        for num in nums:
            temp = max_val
            max_val = max(
                max_val * num, min_val * num, num
            )
            min_val = min(
                temp * num, min_val * num, num
            )
            res = max(res, max_val)
        return res