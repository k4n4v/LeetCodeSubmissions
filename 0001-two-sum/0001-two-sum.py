class Solution(object):
    def twoSum(self, nums, target):
        
        prevMap = {}

        for index, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[n] = index
        return