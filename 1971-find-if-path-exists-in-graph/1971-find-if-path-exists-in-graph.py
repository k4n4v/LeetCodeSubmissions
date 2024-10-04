
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 1. DFS with recursion
        # 2. DFS with stack (iterative)
        # 3. BFS with deque
        
        if source == destination: # base case
            return True
        
        # Adjacency list using dict
        graph = defaultdict(list)
        
        for u, v in edges: # u and v are the two nodes (or vertices) connected by an edge.
            graph[u].append(v)
            graph[v].append(u) # because bi-dircetional

        seen = set()
        seen.add(source)
        stack = [source]
        
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)
                    
        return False
        
        # Time: O(N + E)
        # Space: O(N + E)
        
#         def dfs(i):
#             if i == destination:
#                 return True
            
#             for nei_node in graph[i]:
#                 if nei_node not in seen:
#                     seen.add(nei_node)
#                     if dfs(nei_node):
#                         return True
#             return False
        
        