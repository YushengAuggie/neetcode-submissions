class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        leftMax = height[0]
        rightMax = height[-1]

        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            print(l, r)
            print(f"{leftMax=}, {rightMax=}")
            if leftMax < rightMax:
                l += 1
                if height[l] > leftMax:
                    leftMax = height[l]
                else:
                    res += leftMax - height[l]
            else:
                r -= 1
                if height[r] > rightMax:
                    rightMax = height[r]
                else:
                    res += rightMax - height[r]
        return res


