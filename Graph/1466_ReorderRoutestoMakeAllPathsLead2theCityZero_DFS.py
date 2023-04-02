
#using DFS to solve the 1466 problem on leetcode website


#using DFS to solve the 1466 problem on leetcode website

import unittest
from collections import defaultdict

import unittest
from collections import defaultdict

class Solution:

    #def __init__(self):
    #    self.ans = 0

    
    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        #create a graph or adj matrix

        graph = defaultdict(list)

        for curr_node, nb_node in connections:
            #we also add a sign (1 or 0)in order to know the the way between two cities
            graph[curr_node].append([nb_node, 1])
            graph[nb_node].append([curr_node, 0])


        visited = set()
        ans = 0
        
        def dfs(curr_node):
            nonlocal ans
            visited.add(curr_node)

            for nb_node, sign in graph[curr_node]:
                
                if nb_node not in visited:
                    #increase ans because our sign only can be 0 or 1, so we do not need to check whether it is -> or <-
                    #and please remember that: n-1 edge, n cities, that mean 0 circle in the graph
                    ans += sign
                    visited.add(nb_node) # visited[nb_node] = true; C++
                    dfs(nb_node)
            
        
        dfs(0)

        return ans


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.minReorderObj = Solution()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_minReorder(self):

        n = 6
        connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
        self.assertEqual(self.minReorderObj.minReorder(n, connections), 3)
         
        m = 5
        connections_m = [[1,0],[1,2],[3,2],[3,4]]
        #print("n = ", connections)
        #print(self.minReorderObj.minReorder(n, connections))
        self.assertEqual(self.minReorderObj.minReorder(m, connections_m), 2)


        n = 2
        connections = [[1,0],[2,0]]
        self.assertEqual(self.minReorderObj.minReorder(n, connections), 0)
        
        n = 2
        connections = [[1,0],[2,0]]
        self.assertEqual(self.minReorderObj.minReorder(n, connections), 1)
        

if __name__ == '__main__':

    unittest.main()

       
        
       