class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        time: O(n)
        space: O(1)
        """
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    res[i] = j - i
                    break
                elif temperatures[i] >= temperatures[j]:
                    if res[j] == 0:
                        res[i] = 0
                        break
                    j = res[j] + j
        return res

