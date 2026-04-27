class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        binary search
        min_k = 1
        max_k = max(piles)

        The smallest k that can meet condition ->
        add(piles[i]/k + 1 if piles[i] % k == 0) <=h

        time: O(n*logm) n is the length of piles, m is the largest value in piles
        space: O(1)
        """

        min_k = 1
        max_k = max(piles)
        res_k = max_k

        def is_valid_k(k: int) -> bool:
            print("check k valid", k, end=" ")
            hours = 0
            for pile in piles:
                if pile % k != 0:
                    hours += 1
                hours += pile // k 
                if hours > h:
                    print("False")
                    return False
            print("True")
            return True

        while min_k <= max_k:
            mid_k = (min_k + max_k) // 2
            if not is_valid_k(mid_k):
                min_k = mid_k + 1
            else:
                res_k = min(res_k, mid_k)
                print("res_k, ", res_k)
                max_k = mid_k - 1
        return res_k

