class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        time: O(n^2)
        space: O(1)
        """ 
        if len(s) == 1:
            return s
        max_str = ""
        # odd length polindrom
        for i in range(len(s)):
            left = i
            right = i
            print(i, left, right, s[i])
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if right - left + 1 > len(max_str):
                    max_str = s[left:right + 1]
                left -= 1
                right += 1
        
        # even length polindrom
        for i in range(len(s)):
            left = i
            right = i + 1
            print(i, left, right, s[i])
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if right - left + 1 > len(max_str):
                    max_str = s[left:right + 1]
                left -= 1
                right += 1
                
        
        return max_str


