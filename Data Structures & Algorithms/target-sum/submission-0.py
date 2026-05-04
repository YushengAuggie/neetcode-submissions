class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        so for each element, we can either choose + or -
        then the brute force way is just to get all combinations. 
        and if we want, we can have memorization and say, prev + [idx:]
        the sub problem could be target + [idx:], base is 0 from idx == len(nums)

        time: O(2^n) -> O(n)
        space: O(1) -> O(2^n)
        """


        mem = {}
        
        def dp(idx: int, cur_target:int) -> int:
            if idx == len(nums):
                return 1 if cur_target == 0 else 0
            if (idx, cur_target) in mem:
                return mem[(idx, cur_target)]
            
            cur = nums[idx]
            plus = dp(idx + 1, cur_target + cur)
            minors = dp(idx + 1, cur_target - cur)
            mem[(idx, cur_target)] = plus + minors
            return mem[(idx, cur_target)]
        
        return dp(0, target)
            
                



       