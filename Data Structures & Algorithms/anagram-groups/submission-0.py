from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaragam_dict = defaultdict(list)
        for word in strs:
            primary_anagram = "".join(sorted(word))
            anaragam_dict[primary_anagram].append(word)

        return list(anaragam_dict.values())