class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_val = nums[0]
        cur_val = 0
        for n in nums:
            if n + cur_val > 0 or n + cur_val > max_val:
                cur_val += n
                max_val = max(max_val, cur_val)
            else:
                cur_val = 0
        return max_val
            
