class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # use O(1) space and O(n) time complexity
        prefix = 1
        product_list = [1] * len(nums)
        for idx, num in enumerate(nums):
            product_list[idx] = prefix
            prefix = prefix * num
        
        suffix = 1
        for idx in range(len(nums) - 1, -1, -1):
            product_list[idx] = suffix * product_list[idx]
            suffix = suffix * nums[idx]
            
        return product_list
