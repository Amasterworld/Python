"""
2360. Longest Cycle in a Graph

You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.
"""


"""
SOLUTION:   - it is directed graph (1)
            - each node has at most one outgoing edge(2)
(2) is very important, because it  ensure that one node only involves to the one circle (no more edge to involve)
-> we can use DFS  algorithm to solve this problem, traverse all nodes by their edges, if edges[curr_node] != -1 then 
keep traversing(DFS) and count and keep update the number of edge for each circle. 
- one of the problem we need to solve: how to calculate the lenght of each circle for example 6>1>0>3>2>4>3
that mean the length of the circle only is 3 (3>2>4>3) not from 6 to handle this problem  we create a container (list, unordered_map...)
namely, dist, to contain the distance from node -> nb_node_1->nb_node_2->... and then whenver nb_node_n == node again(cirlce)
we calculate len_cir =  dist[nb_node_n] - dist[node] + 1;

"""
import unittest
from collections import defaultdict
class Solution:
    def longestCycle(self, edges: list[int]) -> int:        
        
        ans = -1 # that mean we have 0 circle
        n = len(edges)
        #track the visited nodes
        visited = set() # to track visited nodes
        #container to keep dist between nodes      
        
        #traverser all nodes       

        def dfs(curr_node):
            
            nonlocal ans
            visited.add(curr_node)
            nb_node = edges[curr_node]            
           
            # if has an outgoing edge from curr_node
            if nb_node != -1 and nb_node not in visited: #..... !visited[nb_node]
                
                dist[nb_node] = dist[curr_node] + 1
                #print("distance ", dist)
                dfs(nb_node) 
            #if a circle is made, 
            elif nb_node != -1 and dist[nb_node]: # cond: nb_node in visited is implicitly
                #print("curr_node ", curr_node, "nb node", nb_node)
                ans = max(ans, dist[curr_node] - dist[nb_node] + 1)

        for node in range(n):            
            if node not in visited:

                dist = defaultdict(list) # dist should be reseted for each unvisited  node
                dist[node] = 1
                dfs(node)

        return ans
                

class TestSolution(unittest.TestCase):

    def setUp(self):
        #create an object to access the methods
        self.longest_cycle = Solution()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_ex1(self):
        
        edges = [3,3,4,2,3]
        self.assertEqual(self.longest_cycle.longestCycle(edges), 3)

    def test_ex2(self):
        
        edges = [2,-1,3,1]
        self.assertEqual(self.longest_cycle.longestCycle(edges), -1)

    def test_ex3(self):
        
        edges = [-1,4,-1,2,0,4]
        self.assertEqual(self.longest_cycle.longestCycle(edges), -1)

    def test_ex4(self):
        
        edges = [3,4,0,2,-1,2]
        self.assertEqual(self.longest_cycle.longestCycle(edges), 3)

if __name__ == '__main__':
    unittest.main()
        
