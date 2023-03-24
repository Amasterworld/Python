
"""
Created on Fri Mar 24 08:44:25 2023

@author: phuongduongbich
"""

"""
1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:


Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

"""


"""
SOLUTION: n nodes, and n-1 edges, that mean 0 circle in the connection such as: 2<-3<-1 and 2->1, so we have 3 nodes but need 3 edges

because 0 circle in the connection that mean always has only 1 way from left to node 0
-> make a sign in the graph to know that the path is from node a to b or vice versus
whenever meet the oppite sign then +1
-> hence the solution to solve this problem can be used DFS or BFS

"""
import unittest
from collections import defaultdict
from collections import deque

class Solution:
    
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
    
        graph = defaultdict(list)
        
        for curr_node, nb_node in connections:

            #should add the sign to know from city a to b or from b to a
            graph[curr_node].append([nb_node, 1])
            graph[nb_node].append([curr_node, 0])
        
        ans = 0
        
        def bfs():
            
            nonlocal ans
            q = deque([0])
            visited = set()
            visited.add(0)
            while q:
                
                curr_node = q.popleft()
                
                for nb_node, sign in graph[curr_node]:
                    
                    if nb_node not in visited:
                        
                        visited.add(nb_node)
                    #here, one sign is 0 and another one is 1, because + 0 does not change the count value hence:
                        ans += sign
                        q.append(nb_node)
                    
                        
                    
        bfs()            
        return ans             
    
#test
class TestSolution(unittest.TestCase): # TestSolution inherits from unittest.TestCase
    
    def setUp(self):
        #create an object so, we can access the method of Solution class
        self.solution = Solution()
    
    def test_minReorder(self):
        
         n = 6
         connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
         
         self.assertEqual(self.solution.minReorder(n, connections), 3)
         
        
         n = 5
         connections = [[1,0],[1,2],[3,2],[3,4]]
         
         self.assertEqual(self.solution.minReorder(n, connections), 2)
         
         #intended to compare with 1, we can easily see that python test gives us an error
         n = 2
         connections = [[1,0],[2,0]]
         
         self.assertEqual(self.solution.minReorder(n, connections), 1)

if __name__ == '__main__':
    unittest.main()
    
        
            
                
        