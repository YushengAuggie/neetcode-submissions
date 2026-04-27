class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        O(1) time
        O(n) space (len(nums))
        put the number to the [0] * 10001
        and if find the duplicate, that is the duplicated number
        """ 
        ary = [0] * (len(nums) + 1)
        for n in nums:
            if ary[n] == n:
                return n
            else:
                ary[n] = n
        return 0
        