class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        time: O(n * 2^n) n is from copy, and we have 2^n subset
        space: O(n) (not include output, otherwise O(n*2^n))
        """
        res = [[]]
        def generate(idx:int, cur: List[int]) -> None:
            if idx == len(nums):
                return
            
            num = nums[idx]
            # add it 
            cur.append(num)
            res.append(cur[:])
            generate(idx + 1, cur)

            # skip it
            cur.pop()
            generate(idx + 1, cur)
            return

        generate(0, [])
        return res
