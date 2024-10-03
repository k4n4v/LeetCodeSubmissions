class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        
        for i, op in enumerate(operations):
            
            if op == "C":
                stack.pop()
                
            elif op == "D":
                stack.append(stack[-1]*2)
                
            elif op == "+":
                stack.append(stack[-1]+stack[-2])
                
            else:
                stack.append(int(op))
        
        return sum(stack)
    
        # Time: O(n)
        # Space: O(n) 