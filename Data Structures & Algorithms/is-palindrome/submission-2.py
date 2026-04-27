class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                # print(s[left]," x ", s[right])
                return False
            else:
                # print(s[left],"=", s[right])
                left += 1
                right -= 1
        return True