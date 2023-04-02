"""
787. Cheapest Flights Within K Stops

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1. 

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

"""

"""
SOLUTION: this problem can be solved by using Bellar-Ford algorithm, but it is a bit slow
in this solution: I used Dijkstra's algorithms that can guarantee that we can reach dst node with lowest weight
but we also need to check the condition the kth stop
"""
from math import inf
from queue import Empty, Queue 
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        #create graph or adjust matrix, 
        graph =[[] for i in range(n)]; #graph is list of list with n slots
        for f in flights:
            graph[f[0]].append((f[1], f[2]));


        dist = [inf]*n; # create dist to store price from src city to all cities, the initial values are infinity values

        q_city_price = Queue(); #queue to contain city and price to reach the current city
        q_city_price.put((src, 0)); # add src city, and its price == 0 to the queue, note queue is FIFO
        dist[src] = 0;
        stop = 0;
        
        while stop <= k and q_city_price.empty() == False:

            size_q = q_city_price.qsize();
            while size_q > 0:

                curr_city, curr_price = q_city_price.get(); #c++ .fron and .pop(), in Python .get() is a combination of front and pop()

                for neighbor, price2neigbor in graph[curr_city]:
                    total_price = price2neigbor + curr_price; 
                    #if we found the path to reach neighbor with lower price then update, and also add its next neighbors to queue
                    if total_price < dist[neighbor]:
                        dist[neighbor] = total_price;
                        q_city_price.put((neighbor, price2neigbor));
                size_q -= 1;
            #whenever move to the next city, should increase stop in order to get the smallest stop
            stop += 1;

        return dist[dst] if dist[dst] != inf else -1  