from collections import defaultdict

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        # brute force:
        find all substrings for i for j (n^2 ) and then check polidrome -> O(n^3)

        # if the current s[i] == s[j] and dp[i+1][j-1] == True
         then it is a polidrome
        time: O(n^2 to compare all the characters, + n count polidrome for all letters expand)
        space: O(n^2) 
        """ 
        dp = defaultdict(bool) # two dimentional dict, i, j -> s[i:j+1] is polindrome
        count = 0
        def is_polindrom(i: int, j:int) -> bool:
            """Is s[i:j +1] is a polidrome. """
            # print("in", i, j)
            if (i, j) in dp:
                return dp[(i,j)]
            if i >= j:
                dp[(i,j)] = True
            elif s[i] == s[j] and is_polindrom(i + 1, j - 1):
                dp[(i,j)] = True
            else:
                dp[(i,j)] = False
            return dp[(i,j)]
                
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_polindrom(i, j):
                    count += 1
        return count
                    
                

