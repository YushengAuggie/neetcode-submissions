class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            cur = digits[i] + carry
            carry = cur // 10
            cur = cur % 10
            digits[i] = cur
        if carry == 1:
            digits = [1] + digits
        return digits
            

