
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
        # state:
        # idx = start index of the next substring to choose
        # prev_list = current palindrome partition built so far
        #
        # transition:
        # choose every possible next substring s[idx:i]
        # if it is a palindrome, include it in the current partition
        # and continue solving from index i

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
            

            
        

