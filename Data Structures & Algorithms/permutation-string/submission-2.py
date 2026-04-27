class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        time: O(n)
        space: O(1)
        """
        if len(s2) < len(s1):
            return False
        s1_c_counts = [0 for _ in range(26)]
        s2_c_counts = [0 for _ in range(26)]

        for i in range(len(s1)):
            s1_c_counts[ord(s1[i]) - ord('a')] += 1
            s2_c_counts[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_c_counts[i] == s2_c_counts[i]:
                matches += 1

        l = 0
        r = len(s1) - 1
        while r < len(s2):
            if matches == 26:
                return True
            
            i_c = ord(s2[l]) - ord('a')
            if s1_c_counts[i_c] == s2_c_counts[i_c]:
                matches -= 1
            s2_c_counts[i_c] -= 1
            if s1_c_counts[i_c] == s2_c_counts[i_c]:
                matches += 1
            l += 1

            r += 1
            if r == len(s2):
                return False
            i_c = ord(s2[r]) - ord('a')
            if s1_c_counts[i_c] == s2_c_counts[i_c]:
                matches -= 1
            s2_c_counts[i_c] += 1
            if s1_c_counts[i_c] == s2_c_counts[i_c]:
                matches += 1

        return matches == 26
