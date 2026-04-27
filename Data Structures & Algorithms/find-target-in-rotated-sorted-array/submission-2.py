class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            # find the sorted half and compare
            # if left side is softed:
            if nums[left] <= mid_val:
                if nums[left] <= target < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid_val < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

