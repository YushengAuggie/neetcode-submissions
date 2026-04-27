class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        # build a set
        sort it first nlog
        and loop through the nums
        always choose
        num + (anything in the set that is <= nums) and till hit the target
            anyone before it or itself 
            we can do a recursion here with idx and target
            if hit, we update the list
        and move to the next number
        """
        ret_list = []
        nums.sort()
        def helper(idx:int, nums:list[int], remaining:int, cur_list:list[int]) -> None:
            # find all the numbers <= nums:
            for i in range(idx + 1):
                if nums[i] > remaining:
                    return 
                new_list = cur_list + [nums[i]]
                if nums[i] == remaining:
                    ret_list.append(new_list)
                    return
                if nums[i] < remaining:
                    helper(i, nums, remaining - nums[i], new_list)
                    
            return

        helper(len(nums) - 1, nums, target, [])
        return ret_list
            
