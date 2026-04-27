class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        find the max product and min product or the ary
        dp[i] = (max_val, min_val) # nums[:i+1] largest and smallest sub-array
        dp[i + 1] = (
            max(
                nums[i],
                dp[i][0]*nums[i],
                dp[i][1]*nums[i]
            ),
            min(
                nums[i],
                dp[i][0]*nums[i],
                dp[i][1]*nums[i]
            )
        dp[len(nums)][0]
        time:O(n)
        space:O(n)
        """
        dp = {} # key: idx, val: max_val, min_val
        max_val = float("-inf")
        
        def helper(i:int) -> tuple[int, int]:
            nonlocal max_val

            if i in dp:
                return dp[i]
            
            if i == 0:
                dp[0] = (nums[0], nums[0])
            else:
                prev_max, prev_min = helper(i - 1)
                dp[i] = (
                    max(
                        nums[i],
                        prev_max * nums[i],
                        prev_min * nums[i]
                    ),
                    min(
                        nums[i],
                        prev_max * nums[i],
                        prev_min * nums[i]
                    )
                )
            max_val = max(max_val, dp[i][0])
            return dp[i]

        helper(len(nums) - 1)
        print(dp)
        return max_val