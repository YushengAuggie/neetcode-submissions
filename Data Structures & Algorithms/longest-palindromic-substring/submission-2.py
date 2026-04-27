class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
         a b a b d
         ^
         ^ 
        """ 
        # def is_palidrom(a: str) -> bool:
        #     return a == a[::-1]
        if len(s) == 1:
            return s
        res = ""
        for i in range(len(s)):
            print(i)
            for j in range(len(s) - 1, i-1, -1):
                print(s[j:i-1:-1])
                print(i, j, s[i:j+1], s[i:j+1][::-1])
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    if len(s[i:j+1]) > len(res):
                        res = s[i:j+1]
        return res
