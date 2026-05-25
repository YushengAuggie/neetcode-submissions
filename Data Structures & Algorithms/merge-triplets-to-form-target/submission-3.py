class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_positions = [False] * 3
        for t in triplets:
            if (
                t[0] > target[0]
                or t[1] > target[1]
                or t[2] > target[2]
            ):
                # not valid, cannot use
                continue

            for position in [0, 1, 2]:
                if t[position] == target[position]:
                    found_positions[position] = True

        return all(found_positions)
        