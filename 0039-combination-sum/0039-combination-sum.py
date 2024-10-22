class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        
        def dfs(start, sol, curr_sum):
            if curr_sum == target:
                res.append(sol.copy())
                return
            if curr_sum > target:
                return
            
            for i in range(start, len(candidates)):
                sol.append(candidates[i])
                dfs(i, sol, curr_sum + candidates[i])
                sol.pop()
        
        dfs(0, sol, 0)
        return res