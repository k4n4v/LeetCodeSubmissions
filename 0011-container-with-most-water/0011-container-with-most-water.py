class Solution:
    def maxArea(self, height: List[int]) -> int:
        # OPTIMIZED SOLUTION (O(n))
        l, r = 0, len(height) - 1
        res = 0
        
        while l < r and r > l:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1
                
        return res
            
    