from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        water = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                water += max(0, leftMax - height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water += max(0, rightMax - height[right])
        return water
