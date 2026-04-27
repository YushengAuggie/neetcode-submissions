class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """ 
        pick_max, skip_max = 0, 0
 
        for i in range(len(nums)):
            dummy = max(pick_max, skip_max)
            pick_max = nums[i] + skip_max
            skip_max = dummy
            # print(nums[i], pick_max, skip_max)

        return max(pick_max, skip_max)
        
        """
                    5. 1. 2. 10  6   2   7.  9    3    1
        pick_max 0. 5. 1. 7. 15  13  17. 20. 26. 23. 27
        skip_max 0. 0. 5. 5. 7.  15. 13. 17. 20. 26. 23
        """