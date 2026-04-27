class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        time: O(n)
        space: O(n)
        """
        mem = {
            0: nums[0]
        }
        def dp(idx:int) -> int:
            if idx in mem:
                return mem[idx]
            
            # till idx, the largest we can get
            # choose all thing before + cur one
            # ignore before and get the current one
            all_before = dp(idx - 1) + nums[idx]
            only_cur = nums[idx]
            mem[idx] = max(all_before, only_cur)
            return mem[idx]
        dp(len(nums) - 1)
        print(mem)
        return max(mem.values())

