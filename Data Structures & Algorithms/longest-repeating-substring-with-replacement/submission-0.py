from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        can I track the c in str
        like 
        dict[c] += 1 
        and use left and right pointer,
        if diff > k:
            we move left += 1 and remove c
        how do we count diff
        we can have a headq to record the max number of c 
        if the current c != max occurance c, then we know ....
        but how do we get the max occurance c
        we can have (c, count), but updating count could be tricky here
        
        replacement_needed = window_size - max_count_in_window

        """
        character_count = defaultdict(int)
        left = 0
        right = 0
        max_len = 0
        max_character_count = 0
        while left <= right and right < len(s):
            character_count[s[right]] += 1
            max_character_count = max(max_character_count, character_count[s[right]])
            print(f"add {s[right]} {character_count[s[right]]=} {max_character_count=}")
            while left <= right and (right - left + 1) - max_character_count > k:
                print(f"{s[right]} {character_count[s[right]]} Exceeds {k}, {max_len=} {s[left:right+1]}")
                print(f"pop out {character_count[s[left]]}, left+1, {character_count[s[left]]=}")
                character_count[s[left]] -= 1
                max_character_count = max(max_character_count, character_count[s[right]])
                left += 1
            max_len = max(right - left + 1, max_len)
            right += 1
        max_len = max(len(s) - 1 - left, max_len)
        return max_len
                    

