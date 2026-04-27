class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = [1] * len(nums)
        suff = [1] * len(nums)
        ret_list = [1] * len(nums)
        for idx in range(1, len(nums)):
            pref[idx] = pref[idx - 1] * nums[idx - 1]
        
        for idx in range(len(nums) - 2, -1, -1):
            suff[idx] = suff[idx + 1] * nums[idx + 1]
        
        #print(pref)
        #print(suff)
        for i in range(len(nums)):
            ret_list[i] = pref[i] * suff[i]
        return ret_list
