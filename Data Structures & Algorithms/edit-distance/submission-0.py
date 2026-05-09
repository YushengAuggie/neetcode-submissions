class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """ 
        This could be solved by DP. 
        Every time we have three choices. 
        Let's start from word one, 
        and every time we have three choices, 
        we either insert, delete, or replace the current character.

        The thing we need to make sure is that 
        we have a way to compare it.
        We can skip it, meaning 
        we might need two pointers: 
        one pointing to word one and another pointing to word two.
        In here, we can use memory. 

        """

        mem = {}

        def dp(idx1: int, idx2: int) -> int:
            if idx1 == len(word1) and idx2 == len(word2):
                return 0
            
            if idx1 == len(word1):
                return len(word2) - idx2
            if idx2 == len(word2):
                return len(word1) - idx1
            
            if (idx1, idx2) in mem:
                return mem[(idx1, idx2)]

            candidates = []
            # same 
            if word1[idx1] == word2[idx2]:
                candidates.append(dp(idx1 + 1, idx2 + 1))

            # insert
            candidates.append(1 + dp(idx1, idx2 + 1))

            # delete
            candidates.append(1 + dp(idx1 + 1, idx2))

            # replace
            candidates.append(1 + dp(idx1 + 1, idx2 + 1))

            mem[(idx1, idx2)] = min(candidates)
            return mem[(idx1, idx2)]
        
        return dp(0, 0)