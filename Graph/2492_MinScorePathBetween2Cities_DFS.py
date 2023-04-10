
"""
Spyder Editor


This is a temporary script file.
"""
from math import inf
from collections import defaultdict

class Solution:
    
    def minScore(self, n : int, roads : list[list[int]]) -> int:
        
        #create a graph or adj matrix
        graph = defaultdict(list)
        
        for curr_node, nb_node, dist in roads:
            
            #note that graph still is an dictionary that mean it has key and value
            # but value here is a list
            
            graph[curr_node].append([nb_node, dist])
            graph[nb_node].append([curr_node, dist])
        
        visited = set()
        ans = inf
        def dfs(curr_node):
            
            nonlocal ans
            for nb_node, dist in graph[curr_node]:
                visited.add(curr_node)
            
                ans = min(ans, dist)
            
                if nb_node not in visited: # if (!visited[nb_node]){}
                    dfs(nb_node)
        dfs(1)
        return ans
            
if __name__ == "__main__":
    
   minScore = Solution()
   
   n1 = 4
   roads1 = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
   print("the minimum score from city 1 to n1 is ", minScore.minScore(n1, roads1))

   n2 = 4
   roads2 = [[1,2,2],[1,3,4],[3,4,7]]
   print("the minimum score from city 1 to n2 is ", minScore.minScore(n2, roads2))       
        
        
        