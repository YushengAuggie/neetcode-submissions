class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existing_num_idx = dict()
        for idx, num in enumerate(nums):
            missing = target - num
            if missing in existing_num_idx:
                return [existing_num_idx[missing], idx]
            else:
                existing_num_idx[num] = idx
        return []