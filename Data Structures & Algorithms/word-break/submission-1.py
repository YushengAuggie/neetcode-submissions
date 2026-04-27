from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        we can have a dictionary
            if remove w from s -> sub:
                sub problem wordBreak(sub, wordDict)
                and if s == ""
                return True
                else:
                    false
            any option will return True
        len(s) * len(wordDict) * t (word match)
        time: O(n*m)
        space: O(n)
        """
        @lru_cache(None)
        def helper(string: str) -> bool:
            print(string)
            if string == "":
                return True
            for w in wordDict:
                if w == string[:len(w)]:
                    print("took", w)
                    if helper(string[len(w):]):
                        return True
            return False
        return helper(s)
