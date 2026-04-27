class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret_list = []
        nums.sort()
        def dfs(idx:int, cur_list:list[int], remain:int) -> None:
            if remain == 0:
                ret_list.append(list(cur_list))
                return
            if idx == len(nums):
                return
            
            if nums[idx] > remain:
                return
            

            cur_list.append(nums[idx])
            dfs(idx, cur_list, remain - nums[idx])
            cur_list.pop()
            dfs(idx + 1, cur_list, remain)
        dfs(0, [], target)
        return ret_list