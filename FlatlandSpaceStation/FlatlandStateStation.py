# naive solution, this solution does not work when n and c are very BIG O(n2)
def flatlandSpaceStations_naive_solution(n, c):
  firstlist = []
      secondlist = []
      for i in range(n):
          for j in c:
              firstlist.append(abs(i-j)) # calculate and add the distance from city i to space stations (SS) j
          print(firstlist)

          temp = min(firstlist)       # find the min distance from the city i to the SSs j
          firstlist = []        # reset this list in order to store the new one

          secondlist.append(temp)   # add the min distance to the second list
      return (max(secondlist))     # find the max distance among the min distance
    # for exampple city = 0 1 2 3 4 5 6 (n), and c = 0 and 5 (SSs are placed at city 0 and 5) 
    
    """
    1s: firstlist = [0,5] min = 0 
    2nd firstlist =[] and then: secondlist add[0] 
    next iteration , firstlist = [1,4] min = 1  
    2nd firstlist =[] and then: secondlist add[0,1]#
    next iteration , firstlist = [2,3] min = 2  
    2nd firstlist =[] and then: secondlist add[0,1,2] 
      and so on, Finally return the max value in the second list 
      """
    
    """
    better SOLUTION O(n)
    
    1st: sort the list c
    c.sort
    2nd: compare the distance from the last city to the nearest SS with the distance of the starting city c(0)
        max_d  = max (c[0], n-1 - c[-1])  #c[-1] == c[len[c] -1 ], n-1 is the number of the last city                             (1)
    
    SO far we know the distance from the city 0 to the starting SS, for example city = 0 1 2 3 4 5 6, c = [3,5] that mean we have c[0] = 3 (distance from the 1st ss to the city 0 = 3)
           and the distance from the last city to the closest SS by this formula: n-1 - c[-1]
           and then from (1) we get the max dist between them.
           NOW, we only need to calculate the distance of the city from c[0] to c[-1], if we see every SS is a node, then the max distance of the cities from c[0] to the c[1] is the c[0] + c[1] //2
        for example  c = [ 1,4,7], city 1 has a ss, also city 4, hence the max dist from city to  ss 1 or 4 should be 4 - 1 //2 = 1 (cities = 1 2 3 4, c= 1 4, 
        uses //2 because we want to take the min value between from the middle city to the SSs (for this example, they are 1 and 4) )
        and then compare this value with the value taken from (1) if it is greater take it otherwise continue calculate the distance from c[1] to c[2] and so
        
        code:  max_d = max (value_bet_nodes, max_d) # note that at the 1st iteration max_d is the value from (1)                 (2)
        
        value_between_nodes are changed, if smaller, then max_d = max_d otherwise max_d = value_between_nodes, and in the next iteration max (value_bet_nodes, max_d), if value_bet_nodes 
        is greater hence max_d = value_bet_nodes and so on
        full code for (2):
                    for i in range(len(c) -1):
                        max_d = max( (c[i+1] - c[i] //2), max_d) # max_d at the 1st iteration is the value from (1), but it can be different in the 2nd iteration if  (c[i+1] - c[i] //2)
                        is > max_d, because now max_d = c[i+1] - c[i] //2.
                        
                     """
    def flatlandSpaceStations(n, c):
      c.sort()   # sort the c
      max_d = max(c[0] - 0, n-1-c[-1]) # find max distance from the starting SS to the city 0 and distance from  the last city to the closest city, but - 0 = DO NO WRITE It
        # hence we delete it if you want
      # calculate distance between "nodes c" and compare with the max_d
      
      for i in range (len(c) - 1):
        max_d = max (c[i+1] - c[i] //2, max_d)                (2)
      return max_d
      
      
      """
      note that if we use (2) for the naive solution it also help us compact the code
      
      
      
        def flatlandSpaceStations_naive_solution(n, c):
  firstlist = []
      secondlist = []
      for i in range(n):
          for j in c:
              firstlist.append(abs(i-j)) # calculate and add the distance from city i to space stations (SS) j
          print(firstlist)

          temp = min(firstlist)       # find the min distance from the city i to the SSs j
          firstlist = []        # reset this list in order to store the new one

          secondlist.append(temp)   # add the min distance to the second list
      return (max(secondlist))     # find the max distance among the min distance
    # for exampple city = 0 1 2 3 4 5 6 (n), and c = 0 and 5 (SSs are placed at city 0 and 5) 
        """
      #now will be
      
   def flatlandSpaceStations_naive_solution(n, c):
      min_d = abs(c[0] -0)
      for i in range(n):
          for j in c:
            
            min_d = min ( (abs(i-j),min_d )
            
    
    
      
