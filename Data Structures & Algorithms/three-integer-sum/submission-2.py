
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # loop through the array nums and get the fixed pair of i, j
        # then the next thing is we just need to get the 
        # target = i + j + n = 0
        # one constrain here is that we cannot have duplicated troplets
        # so n must be unique. 
        # n^2 for finding the pair, and then n -> n^2
        ret_list = []
        nums.sort()
        # print(nums)
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]
                if sum_val == 0:
                    ret_list.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum_val < 0:
                    left += 1
                else:
                    right -= 1
        return ret_list
            