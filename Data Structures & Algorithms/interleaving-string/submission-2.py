class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Now, let's try dynamically picking one letter from S1 and S2. 
        We could dynamically choose the next character from either S1 or S2,
        and then combine them to get S3.

        So if we can start from the beginning and the character is not the same as S3, then we just return. In that case, we can prune some of the leaves.
        """

        if len(s3) != len(s1) + len(s2):
            return False

        mem = {}

        def dp(idx:int, idx1:int, idx2:int) -> bool:
            if idx == len(s3):
                return True
             
            if (idx1, idx2) in mem:
                return False
            
            # either choose idx1 or idx2 for the next character
            if idx1 < len(s1) and s3[idx] == s1[idx1]:
                # we can choose this
                if dp(idx + 1, idx1 + 1, idx2):
                    return True

            if idx2 < len(s2) and s3[idx] == s2[idx2]:
                # we can choose this
                if dp(idx + 1, idx1, idx2 + 1):
                    return True
            
            mem[idx1, idx2] = False
            return False
        return dp(0, 0, 0)
            
