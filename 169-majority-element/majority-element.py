class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        res, maxCount = 0, 0
        
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            res = num if seen[num] > maxCount else res
            maxCount = max(maxCount, seen[num])
        return res