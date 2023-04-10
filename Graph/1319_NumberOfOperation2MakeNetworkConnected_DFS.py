"""
1319. Number of Operations to Make Network Connected

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

Example 1:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1

"""

"""
SOLUTION: if the number of edges < the number of vertices - 1 then we never can connect all vertices together
Otherwise, we can use DFS algorithm to traverse each computer(vertex or node) to all its other connected computers
for example: 1->2>3, 1->3, 3->2,  4->5->6, 7->8->9. Firstly,  that mean: number_of_time+1, then from 1 to all its possible connected comps are 2 and 3.
to avoid infinity loop: mark comp 2 and as visited. Secondly, DFS from 4, number_of_time+1 again, 5,6 are marked as visited also
Finally, DFS from 7 ... remember at the end we should return number_of_time-1; because we always +1 from the beginning even may all comps are connected

"""
from collections import defaultdict
import numpy as np
class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        #if the number of edges < the number of vertex - 1 that mean we never can connnect to all vertices, then return -1
        
        if len(connections) < n - 1: 
            return -1

        #create a graph
        #graph is a dict of list, {curr_node : [nb_node1, nb_node2 ...]} hence graph[curr_node]->access to the value of dict using datatype is a list
        graph = defaultdict(list) 
        for curr_node, nb_node in connections:
            graph[curr_node].append(nb_node)
            graph[nb_node].append(curr_node)
        #C++ vector<vector<int>>graph(n+1), graph[connections[i][1]].emplace_back(connections[i][0]) ;  graph[connections[i][0]].emplace_back(connections[i][1])  

        number_of_time = 0
        visited = set()

        def dfs(curr_node):
            #mark curr_node is visited
            visited.add(curr_node)
            for nb_comp in graph[curr_node]:
                if nb_comp not in visited:
                    dfs(nb_comp)

        for idx_comp in range(n):
            if idx_comp not in visited: # if the computer is not visited then search from it
                number_of_time += 1
                dfs(idx_comp)
        
        
        
        
        return number_of_time - 1
        

if __name__ == "__main__":

    makeConnectedObj = Solution()

    n = 4
    connections = [[0,1],[0,2],[1,2]]

    print("the minimum number of times to connect all comps is ", makeConnectedObj.makeConnected(n, connections) )



                
        
        