class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        slow, fast pointers
        Space: O(1)
        Time: O(n)
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # now we detect the cycle
        slow2 = 0
        while slow != slow2:
            # the next time they meet, it is the duplicate
            # which is the start of the cycle
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow

