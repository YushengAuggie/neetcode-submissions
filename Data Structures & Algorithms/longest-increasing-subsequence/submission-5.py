class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        time: O(n ^2)
        space: O(n)
        """ 
        
        mem = [1] * len(nums)

        # backward
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    mem[i] = max(mem[i], 1 + mem[j])
        # print(mem)
        return max(mem)