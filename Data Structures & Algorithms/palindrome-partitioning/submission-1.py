
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        we can use dp
        we can have a is_palindrome function
        and 
        for every idx mem[start] -> start from a, how many polindrom we can have
        s[start:end] mem[start] + 1 * mem[start+1] + if valid(s[start:2]) s[start:2] * s[start+2] ...
        
        base case: 
        idx == len(s) -> 0
        transition
        if s[start: idx + 1] is valid
        then do dp(idx + 1) lese 1->2 ...

        """
        res = []
        def is_polindrom(substr:str) -> bool:
            return substr == substr[::-1]

        def dp(idx: int, prev_list: List[str]) -> None:
            if idx == len(s):
                res.append(prev_list[:])
                return
            
            # starting from idx
            # what are the valid cases

            for i in range(idx + 1, len(s) + 1):
                if is_polindrom(s[idx: i]):
                    prev_list.append(s[idx:i])
                    dp(i, prev_list)
                    prev_list.pop()
        dp(0, [])
        return res
            

            
        

