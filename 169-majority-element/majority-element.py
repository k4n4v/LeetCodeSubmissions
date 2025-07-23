class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        for num in seen:
            val = seen[num]
            if val > (len(nums) / 2):
                return num