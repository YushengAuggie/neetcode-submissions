from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for c in t:
            dict_t[c] += 1
        
        ans_left = ans_right = 0
        left = right = 0
        min_len = float("inf")
        need = len(dict_t) # how many distinct characters in t
        have = 0 # how many characters are meet the need

        while right < len(s):
            dict_s[s[right]] += 1
            if dict_s[s[right]] == dict_t[s[right]]:
                have += 1
            while have == need:
                # find it
                cur_len = right - left + 1 
                if cur_len < min_len:
                    min_len = cur_len
                    ans_left = left
                    ans_right = right
                dict_s[s[left]] -= 1
                if dict_s[s[left]] < dict_t[s[left]]:
                    have -= 1
                left += 1
            right +=1
        
        return s[ans_left:ans_right + 1] if min_len < float("inf") else ""
