class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Time: O(n^2)
        Space: O(n^2) in the worst case due to duplicate items in next_queue 
        """

        steps = 0
        queue = [0]
        farthest = 0
        visited = set()
        n = len(nums)

        while queue:
            next_queue = []
            while queue:
                cur = queue.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                farthest = max(cur, farthest)
                if farthest >= n - 1:
                    return steps
                for nxt in range(cur + 1, cur + nums[cur] + 1):
                    if nxt not in visited:
                        next_queue.append(nxt)
            queue = next_queue
            steps += 1

        # not able to reach end
        return -1

       