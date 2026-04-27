class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        two pointers l, r -> s2
        for every pointer move, we update the current characters in the window
        time: O(n)
        space: O(1)
        """ 

        if len(s1) > len(s2):
            return False

        
        s1_c_count = [0 for i in range(26)]
        window_c_count = [0 for i in range(26)]
        for i in range(len(s1)):
            s1_c_count[ord(s1[i]) - ord('a')] += 1
            window_c_count[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        r = len(s1) - 1
        
        while r < len(s2):
            if window_c_count == s1_c_count:
                return True
            if r == len(s2) - 1:
                return False
                
            print(chr(ord(s2[l])), "-")
            window_c_count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            print(chr(ord(s2[r])), "+")
            window_c_count[ord(s2[r]) - ord('a')] += 1
            
        return False
