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
        def _contains(dict1, dict2):
            for k2, v2 in dict2.items():
                if dict1[k2] < v2:
                    return False
            return True

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for c in t:
            t_dict[c] += 1

        left = right = 0
        valid_string = ""
        min_len = float("inf")
        while right < len(s):
            s_dict[s[right]] += 1
            while _contains(s_dict, t_dict):
                current_len = right - left + 1
                if current_len < min_len:
                    valid_string = s[left : right + 1]
                    min_len = current_len 
                s_dict[s[left]] -= 1
                left += 1
            right += 1

        return valid_string
