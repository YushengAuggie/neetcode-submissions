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

        while left <= right:
            mid = (right + left) // 2
            if mid == 0:
                left = mid + 1
            if mid == len(nums) - 1:
                break
            elif nums[mid - 1] > nums[mid] and nums[mid + 1] > nums[mid]:
                # hit
                return nums[mid]
            elif nums[right] < nums[mid]:
                left = mid + 1
            elif nums[mid] < nums[left] and nums[mid] < nums[right]:
                right = mid - 1
            else:
                right = mid - 1

        return min(nums[0], nums[-1]) 
        


        
        