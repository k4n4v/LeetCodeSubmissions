class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        
        def backtrack(i):
            if i == n: # base case
                res.append(sol[:]) # append a copy to the result
                return
            
            # don't pick nums[i]
            backtrack(i+1)
            
            # pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res
    
    # Time: O(2^n)
    # Space: O(n)