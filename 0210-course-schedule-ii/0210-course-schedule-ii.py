class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list) 
        order = []
        
        for prereq, course in prerequisites: # create graph
            graph[prereq].append(course)
            
        UNVISITED, VISITING, VISITED = 0, 1, 2
        
        states = [UNVISITED] * numCourses # states in which we are traversing graph
        
        def dfs(i):
            if states[i] == VISITING: # if we have cycle
                return False
            elif states[i] == VISITED: # if you have already seen it
                return True
            
            states[i] = VISITING
            
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            
            states[i] = VISITED
            order.append(i)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return order