class Solution:
    def reverseBits(self, n: int) -> int:
        """
        convert it to str
        revert it
        and convert it to int
        """
        str_binary_n = []
        for _ in range(32):
            str_binary_n.append(n & 1)
            n = n >> 1
        print(str_binary_n)
        res = 0
        for i in str_binary_n:
            res = (res << 1) | i
        return res
            
