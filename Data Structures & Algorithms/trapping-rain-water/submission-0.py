class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]

        heightest = height[0]
        for i in range(1, len(height) - 1):
            left[i] = heightest
            heightest = max(height[i], heightest)
        
        print(left)
        
        heightest = height[-1]
        for i in range(len(height) - 2, 0, -1):
            right[i] = heightest
            heightest = max(height[i], heightest)
        print(right)
        
        water = 0
        
        for i in range(1, len(height) - 1):
            cur = max(min(left[i], right[i]) - height[i], 0)
            print(i, cur)
            water += cur

        return water


            