from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occurance_c = defaultdict(int)

        for c in s:
            occurance_c[c] += 1
        
        for c in t:
            occurance_c[c] -= 1
        
        
        return all(val ==0 for val in occurance_c.values())