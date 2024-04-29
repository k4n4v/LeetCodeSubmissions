class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        for i, num in enumerate(numbers):

            sums = numbers[l] + numbers[r]
            
            if sums == target:
                return [l+1, r+1]
            
            if sums > target:
                r -= 1
                
            if sums < target:
                l += 1
                