class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Space: O(1) - use the given set itself
        Time: O(n)
        """
        nums = [0] + nums
        for idx, n in enumerate(nums):
            next_n = n
            while idx != next_n:
                swap_val = nums[next_n]
                if swap_val == next_n:
                    return swap_val
                nums[next_n] = next_n
                next_n = swap_val
                nums[idx] = swap_val
        return -1