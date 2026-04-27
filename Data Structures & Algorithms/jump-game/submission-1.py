class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        time: O(n)
        space: O(1)
        """
        goal = len(nums) - 1
        while goal > 0:
            # if anyone can reach goal, then jump back to there
            # otherwise -> cannot reach goal -> false
            idx = goal - 1
            while nums[idx] < goal - idx and idx >= 0:
                idx -= 1

            if idx < 0:
                return False
                
            goal = idx
        return True
            



