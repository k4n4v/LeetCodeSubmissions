
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 1. DFS with recursion
        # 2. DFS with stack (iterative)
        # 3. BFS with deque

        if source == destination: # base case
            return True
        
        seen = set() # need to know what nodes we have visted to avoid infiate loop
        graph = defaultdict(list) # adjaceny list to keep track of node to node
        seen.add(source) # starting at source so add to seen
        
        for u, v in edges: # create a graph based on the edge connections
            graph[u].append(v)
            graph[v].append(u) # bi - directional so we need to add v for u
            
        def dfs(node): 
            if node == destination: # we found the destination
                return True
            
            for nei_node in graph[node]: # check the neighbour nodes of the node
                if nei_node not in seen:
                    seen.add(nei_node) # mark that we have seen the node
                    if dfs(nei_node): # search the neighbnour nodes of that node
                        return True # return true if we found it in the neighbours nodes
            return False # did not find
            
        return dfs(source)