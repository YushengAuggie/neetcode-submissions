class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        time: O(n * target) # target is the total_sum // 2
        space: O(n * target)
        """
        sum_total = sum(nums)
    
        if sum_total % 2 == 1:
            return False
        
        mem = {}
        
        def dp(idx: int, left_sum: int) -> bool:
            if (idx, left_sum) in mem:
                return mem[(idx, left_sum)]
                
            
            if left_sum == sum_total/2:
                return True
            
            if idx == len(nums):
                return False

            if left_sum > sum_total/2:
                return False
            
            # choose idx
            if dp(idx + 1, left_sum + nums[idx]):
                return True

            # skip idx
            if dp(idx + 1, left_sum):
                return True
            
            mem[(idx, left_sum)] = False
            return False
        
        return dp(0, 0)

    


        