class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            print(f"{n=}")
            if n in seen:
                return False
            seen.add(n)
            str_n = str(n)
            next_n = 0
            for c in str_n:
                next_n += int(c) * int(c)
            n = next_n
            print(f"{next_n=}")
            print("\n")

        return True



