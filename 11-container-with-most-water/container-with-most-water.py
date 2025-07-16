class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:

            if height[left] < height[right]:
                container = height[left] * (right - left)
                res = max(res, container)
                left += 1
            else:
                container = height[right] * (right - left)
                res = max(res, container)
                right -= 1

        return res