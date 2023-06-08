class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        numsSet = set(nums)
        
        return True if len(numsSet) != len(nums) else False