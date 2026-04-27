class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = {}
        
        def dfs(idx:int) -> bool:
            if idx == len(nums) - 1:
                return True
            
            if idx in mem:
                return mem[idx]
            
            for i in range(1, nums[idx] + 1):
                if dfs(idx + i):
                    mem[idx] = True
                    return mem[idx]

            mem[idx] = False
            return mem[idx]
        return dfs(0)