class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        fathest = 0
        steps = 0
        n = len(nums)

        while fathest < n - 1:
            for i in range(l, r + 1):
                fathest = max(fathest, nums[i] + i)
        
            if fathest == r:
                return -1
            l = r + 1
            r = fathest
            steps += 1
    
        return steps
    


