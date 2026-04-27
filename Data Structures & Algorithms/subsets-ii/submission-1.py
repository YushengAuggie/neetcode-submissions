class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        The first thing that comes to my mind is just to use DFS 
        And every time we pick one of the rest of the array, one element from there, that can give us a valid combination and we save it 
        And that's it. We just saved all the combinations 
        time: O(2^n * n)
        space: O(n) -> without output 
        space: O(2^n * n) -> output 

        idx       0.   1     2
        prev_nums [].  [7].  [7] [7, 7]
        res.      [].  [7].  [7] [7, 7]
        """

        res = []
        nums.sort()

        def dfs(prev_nums: List[int], idx: int) -> None:
            if idx == len(nums):
                res.append(prev_nums[:])
                return
            
            # choose
            prev_nums.append(nums[idx])
            dfs(prev_nums, idx + 1)
            prev_nums.pop()
            
            # skip
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(prev_nums, idx + 1)


        dfs([], 0)
        return res