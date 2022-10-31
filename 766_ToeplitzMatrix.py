#SOLUTION: the same C++version, note that ; at the end of lines are not necessary, 
# 
class Solution:
            
    
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        r = len(matrix);
        c = len(matrix[0]);
        
        for  i in range (0, c):
            
            if (not self.checkDiag(matrix, 0, i) ):
                return False;
        
    
        for  j in range (1, r):
            if (not self.checkDiag(matrix, j, 0)):
                return False;
            
        
        return True;
    
    def checkDiag(self, matrix: List[List[int]], x, y ) -> bool:
        
        init_val = matrix[x][y];
        r = len(matrix);
        c = len(matrix[0]);
        
        while r > x and c > y:
            if matrix[x][y] != init_val:
                return False;
            x += 1;
            y += 1;
        return True;
    
    # better solution, note that we also can use hash table - dict to solve this problem to store group[r-c] (r1-c1 == r2-c2) hence two cell in the same
    # diagonal: 0-0 == 1-1, then we collect all value r-c, if group[r-c] != ini_val -> return false
    #class Solution(object):
   #
    # def isToeplitzMatrix(self, matrix):
    #    return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
     #              for r, row in enumerate(matrix)
      #             for c, val in enumerate(row))
    #
