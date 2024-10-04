class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        
        for tok in tokens:
            if tok in '+/*-':
                b, a = stk.pop(), stk.pop()
                
                if tok == '+':
                    stk.append(a + b)
                
                if tok == '-':
                    stk.append(a - b)
                    
                if tok == '*':
                    stk.append(a * b)
                    
                if tok == '/':
                    div = a / b
                    if div < 0:
                        stk.append(ceil(div))
                    else:
                        stk.append(floor(div))
            else:
                stk.append(int(tok))
                
        return stk[0]
    
    # Time: O(n)
    # Space: O(n)