class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product = 1
        count_zero = 0
        for num in nums:
            if num != 0:
                all_product *= num
            else:
                count_zero += 1
                if count_zero >= 2:
                    return [0 for _ in nums]
            
        new_list = []
        for num in nums:
            if num != 0:
                if count_zero == 1:
                    new_list.append(0)
                else:
                    new_list.append(int(all_product/num))
            else:
                new_list.append(all_product)
        return new_list
