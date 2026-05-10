class Solution:
    def jump(self, nums: List[int]) -> int:
        """

        """

        steps = 0
        queue = [0]
        farest = 0
        visited = set()
        n = len(nums)

        while queue:
            next_queue = []
            while queue:
                cur = queue.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                farest = max(cur, farest)
                if farest >= n - 1:
                    return steps
                for nxt in range(cur + 1, cur + nums[cur] + 1):
                    if nxt not in visited:
                        next_queue.append(nxt)
            queue = next_queue
            steps += 1

        # not able to reach end
        return -1

       