class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        value = 0
        
        for op in operations:
            if "++" in op:
                value += 1
            elif "--" in op:
                value -= 1
        
        return value