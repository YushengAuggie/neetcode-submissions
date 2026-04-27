
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        we can use dp
        we can have a is_palindrome function
        and 
        for every idx mem[start] -> start from a, how many polindrom we can have
        s[start:end] mem[start] + 1 * mem[start+1] + if valid(s[start:2]) s[start:2] * s[start+2] ...
        
        Backtracking solution.
        
        State:
        - idx: the starting index of the next substring to pick
        - prev_list: the current partition built so far
        
        Base case:
        - when idx == len(s), we have used the whole string,
          so prev_list is a valid palindrome partition
        
        Transition:
        - from idx, try every possible substring s[idx:i]
        - if s[idx:i] is a palindrome, add it to the current partition
          and recurse from index i

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
            

            
        

