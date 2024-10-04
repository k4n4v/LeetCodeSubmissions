class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stk = []
        
        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t: # while the top of the stack has a temp that is smaller than the current temp
                stk_t, stk_i = stk.pop()
                res[stk_i] = i - stk_i
                
            stk.append((t, i))
            
        return res
    
    # Time: O(n), while loop doesnt matter because "put on 'n' things and take off 'n' things"
    # Space: O(n)