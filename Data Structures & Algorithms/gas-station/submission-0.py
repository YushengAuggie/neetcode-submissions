class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def is_valid(i:int) -> bool:
            total = 0
            while i < len(cost):
                total += diff[i]
                if total < 0:
                    return False
                i += 1
            return True

            


        if sum(cost) > sum(gas):
            return -1

        diff = [g - c for g, c in zip(gas, cost)]
        for i in range(len(diff)):
            # try all diff[i] >= 0
            if diff[i] >= 0 and is_valid(i):
                return i
        return -1
                

