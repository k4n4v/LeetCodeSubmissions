class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort() # takes O(nlogn) time
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = num + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
    
    # total time complexity O(nlogn) + n^2 = O(n^2)
    # space could be O(n) or O(1) based on sorting in library
    