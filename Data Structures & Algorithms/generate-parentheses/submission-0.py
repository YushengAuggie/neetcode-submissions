class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        condition n >= left >= right
        dfs 
        time: O(2^n)
        space: O(n)

        """
        
        res = []
        def dfs(diff:int, current_list: List[str]) -> None:
            if len(current_list) == n * 2:
                if diff == 0:
                    res.append("".join(current_list))
                return
            
            if diff > 0:
                current_list.append(")")
                dfs(diff - 1, current_list)
                current_list.pop()
            if diff <= n:
                current_list.append("(")
                dfs(diff + 1, current_list)
                current_list.pop()
        
        dfs(0, [])
        return res