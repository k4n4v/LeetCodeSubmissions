class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1} # base cases, f(0) = 0, f(1) = 1
         
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
        
        return f(n)
            