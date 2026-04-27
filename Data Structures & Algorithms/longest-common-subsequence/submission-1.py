class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        dp
        time: O(n * m)
        space: O(n * m)
        """

        mem = {}

        def dp(p1: int, p2: int) -> int:
            """
            return the longestCommonSubsequence length from p1: and p2:
            """
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            if (p1, p2) in mem:
                return mem[(p1, p2)]

            if text1[p1] == text2[p2]:
                mem[(p1, p2)] = 1 + dp(p1+1, p2+1)
            else:
                mem[(p1, p2)] = max(
                    dp(p1+1, p2),
                    dp(p1, p2+1)
                )
            return mem[(p1, p2)]
        
        return dp(0, 0)

