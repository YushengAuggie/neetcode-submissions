from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            count = [0] * 26 
            for c in word:
                count[ord(c) - ord("a")] += 1
            anagram_dict[str(count)].append(word)
        return list(anagram_dict.values())
            
