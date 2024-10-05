class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        seen = set()
        graph = defaultdict(list)
        
        for a, b in prerequisites:
            graph[a].append(b)
            
        UNVISTED = 0
        VISTING = 1
        VISTED =2
        states = [UNVISTED] * numCourses
        
        def dfs(node):
            state = states[node]
            if state == VISTED: return True
            elif state == VISTING: return False
            
            states[node] = VISTING
            
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            states[node] = VISTED
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
    
    # Time: O(N + E)
    # Space: O(N + E)