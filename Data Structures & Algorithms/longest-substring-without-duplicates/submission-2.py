class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        we can have two pointers.
        left and right, and put all the characters into one set. 
        if the character already in the set, the move the left pointer to right till the duplicated character is not there anymore.
        """

        if len(s) < 2:
            return len(s)
        
        left = 0
        right = 1
        max_len = 0
        contains = set()
        contains.add(s[0])
        """
             z x y z x y z
        idx. 0 1 2 3 4 5 6
        left         ^
        right.           ^
        contains:{
            x
            z
            y
        }
        max_len = 6 - 4 + 1 = 3

        x x x x


        """
        while right < len(s) and left <= right:
            print(f"current constians: {contains}")
            print(f"{left=} {right=} current right {s[right]}")
            if s[right] in contains:
                contains.remove(s[left])
                print(f"Pop out {s[left]=} {contains}")
                left += 1
                max_len = max(right - left + 1, max_len)
                print(f"{max_len=}")
            else:
                contains.add(s[right])
                print(f"add {s[right]=} {contains}")
                right += 1
                print("right += 1")
                
            
            
            print("")
        max_len = max(len(contains), max_len)
        return max_len