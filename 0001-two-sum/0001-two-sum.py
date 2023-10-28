class Solution(object):
    def twoSum(self, nums, target):
        
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1+1:]):
                result = num1 + num2 
                if result == target:
                    return [index1, index1+index2+1]
