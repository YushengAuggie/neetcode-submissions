class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Choose this or not
            maintain the largest number before this when choose this 
            but how can we know what is the longest increasing subsequence?

            len 1 -> 1
            len 2 -> choose first one  cmp 2
                        skip 1, 2
            len n -> chose n cmp n-1 max
                        skip n  n + 1
            len (end) -> if can choose -> return 1

            time: O(n)
            space: O(n)
        """
        def helper(i: int, max_val: int) -> int:
            """
            i: index
            max_val: max_val so far
            @return Longest increasing subsequence from here
            """
            if i == len(nums):
                return 0
            cur_val = nums[i]
            skip_count = helper(i + 1, max_val) 
            choose_count = 1 + helper(i + 1, cur_val) if cur_val > max_val else 0
            return max(skip_count, choose_count)
        return helper(0, -1001)

