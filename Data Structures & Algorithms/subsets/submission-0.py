import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def generate(idx:int, cur: List[int]) -> None:
            if idx == len(nums):
                return
            
            num = nums[idx]
            # add it 
            cur.append(num)
            res.append(copy.deepcopy(cur))
            generate(idx + 1, cur)

            # skip it
            cur.pop()
            generate(idx + 1, cur)
            return

        generate(0, [])
        return res
