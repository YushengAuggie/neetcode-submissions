from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Brute force solution is getting all the substrings and compare it with t
        The time complexity would be:
        len(s) = n
        len(t) = m
        n^2 (all substrings) + m (comparison)
        
        optimized solution1:
        compare left pointer from s with the start of t
        if we catch one, then we continue the comparison
        n * m

        """
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for c in t:
            t_dict[c] += 1

        need = len(t_dict) # how many unique characters in t
        have = 0 # how many characters are meet the need (with frequency)
        left = right = 0
        ans_left = ans_right = 0
        min_len = float("inf")

        while right < len(s):
            s_dict[s[right]] += 1
            if s_dict[s[right]] == t_dict[s[right]]:
                have += 1
            
            while need == have:
                current_len = right - left + 1
                if min_len > current_len:
                    ans_left = left
                    ans_right = right
                    min_len = current_len

                s_dict[s[left]] -= 1
                if s_dict[s[left]] < t_dict[s[left]]:
                    have -= 1
                left += 1

            right += 1

        return s[ans_left : ans_right + 1] if min_len != float("inf") else ""
