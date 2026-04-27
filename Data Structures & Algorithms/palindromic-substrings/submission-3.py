class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        expand from center
        time: O(n^2)
        space: O(1)
        """
        count = 0
        # odd number length
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            count += 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        
        # even
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count


        