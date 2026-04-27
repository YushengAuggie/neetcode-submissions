class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # dp
        # sub problem
        # choose i as the first value, and we combine it with the rest of the values
        # and we keep doing in it
        # till
        # last value in nums
        # and every time we have one valid case we add it to res
        # time:O(n * n!)
        # space: O(n) # without output
        # space: O(n*n!) with output
        def dp(before_nums: List[int], idx: int) -> None:
            if idx == len(nums):
                res.append(before_nums[:])
                return
            
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                before_nums.append(nums[idx])
                dp(before_nums, idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]
                before_nums.pop()
            return
        dp([], 0)
        return res



        
     