class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        time: O(n*2^n)
        space: O(n)
        """
        res = []
        candidates.sort()
        def dfs(idx: int, cur_list: list[int], cur_target:int) -> None:
            if cur_target == 0:
                res.append(cur_list[::])
                return
            if cur_target < 0 or idx == len(candidates):
                return

            # choose cur
            cur = candidates[idx]
            cur_list.append(cur)
            dfs(idx + 1, cur_list, cur_target - cur)
            cur_list.pop()
            
            # skip cur
            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            dfs(idx + 1, cur_list, cur_target)
            return

        dfs(0, [], target)
        return res
            
