class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        def count_one(i: int) -> int:
            count = 0
            while i:
                if 1 & i:
                    count += 1
                i = i >> 1
            return count

        for i in range(n+1):
            count = count_one(i)
            res.append(count)
        return res