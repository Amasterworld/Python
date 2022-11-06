#899. Orderly Queue - leetcode

#the detail algorithm to solve this problem was presented in C++ version
#if k >= 2 the result  == when we sort the given string s
#if  k == 1 the algorithm is very simple step by step move the 1st char and append it at the end of the 
# the string and compare to get what is minimum string
#note that the TC is O(n*n) not n*logn
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
        if k >=2:
            
            return "".join(sorted(s));
        min_lex = s;
        
        for i in range(len(s)):
            
            min_lex = min(min_lex, s[i:] + s[:i]);
            # more pythonic:
        #return min([i:] + s[:i] for i in range(len(s)));
        return min_lex;
