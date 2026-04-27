class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        brute force
        iterate the whole array and get the min value,
        and the min value is the one we return
        return min(nums)
        time: O(n) space: O(1)

        ----
        a better solution
        log n -> binary search
        but how do we use binary search to get the min value, especially the
        array is not sorted ...

        we need to find the place nums[i-1] > nums[i] < nums[mid + 1] --> nums[i] is smallest number
        # left > right -> target is in middle
        # left < right -> target can be left or right 

        """

        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1

        while left < right:
            # bounary
            # when find a condition meet (martch), 
            # there could be another condition meet
            mid = (right + left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
        


        
        