class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        # 1. want to find closet number to 0
        # 2. check if the closet number to 0 is less than 0 and if it is check if the positive version exists
        # if it does, then return the positive version
        
        res = nums[0]
        for i in range(len(nums)):
            if abs(nums[i]) < abs(res):
                res = nums[i]
            
        if res < 0 and abs(res) in nums:
            return abs(res)
        else:
            return res