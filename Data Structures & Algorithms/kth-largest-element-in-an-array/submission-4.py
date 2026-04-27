class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        We can pick an element from nums
        And then get the numbers less than it 
        If the number of items less than or equal to it is k-1, then that's the target value 
        If the number of items less than or equal to this item is smaller than k,  then we get a larger number from the right side
        If the number of items less than or equal to this item is larger than k, then we keep doing it from the left side
        Time complexity for this is on average O(n), in the worst case O(n^2), and the space complexity is O(n) 
        """
        def get_split(array: list[int], num: int) -> tuple[list[int], list[int]]:
            left = []
            right = []
            for a in array:
                if a < num or a == num:
                    left.append(a)
                else:
                    right.append(a)
            return left, right
            

        if len(nums) < k:
            return -1
        next_array = [i for i in nums]
        target = k
        while next_array:
            num = next_array[0]

            left, right = get_split(next_array[1:], num)
            if len(right) == target - 1:
                return num
            elif len(right) < target:
                next_array = left 
                target = target - len(right) - 1 # num + left are not possible
            else:
                next_array = right
        return -1
            