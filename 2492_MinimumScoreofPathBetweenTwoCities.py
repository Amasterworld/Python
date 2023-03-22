"""
2492. Minimum Score of a Path Between Two Cities

You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.
The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n. 

Example 1:

Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.

Example 2:

Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
"""

"""
SOLUTION: with this kind of problem, 1st step always is create a graph or adj matrix
then depends on the problem can use:  DFS, BFS, Djistra, Union or A star ... to solve the problem.
- for this problem we need to traverse to all nodes and get the smallest distance from node 1 to node n
then DFS, OR BFS can be used.


"""
from math  import inf
from collections import deque
from termios import NL1
class Solution:

    def minScore(self, n: int, roads: list[list[int]]) -> int:

        
        #create a blank graph or adj matrix with n slots for appending late
        # in C++ std::vector<vector<int>>graph(n+1);
        graph = [[] for _ in range(0, n+1)]

        for node, nb_node, dist in roads:

            graph[node].append((nb_node, dist))
            #note that this grpah is bidirection
            graph[nb_node].append((node, dist))

        def bfs() -> int:
            ans = inf
            #insert node 1

            q = deque([1])
            visited = set()
            while q: # == while(!q.empty()) in C++
                #here we use deque as a queue: FIFO, hence use popleft medthod
                curr_node = q.popleft();
                #in Python popleff() = q.front() + q.pop();
                visited.add(curr_node)
                for nb_node, dist in graph[curr_node]:
                    
                    ans = min(ans, dist)
                    # if nb_node is visited b4 then ignore it
                    if nb_node in visited:
                        continue
                    q.append(nb_node)
            return ans
        answer = bfs()
        return answer

if __name__ == "__main__":
    
    minScore = Solution()
    
    n1 = 4
    roads1 = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
    print("the minimum score from city 1 to n1 is ", minScore.minScore(n1, roads1))

    n2 = 4
    roads2 = [[1,2,2],[1,3,4],[3,4,7]]
    print("the minimum score from city 1 to n2 is ", minScore.minScore(n2, roads2))
                    
                    




