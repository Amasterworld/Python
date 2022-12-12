class Solution:
    def climbStairs(self, n : int) -> int:
        
        dp = [None]*(n+1); # # create a list with size = n+1, ele = None
        dp[1] = 1; # based condition
        #when n == 1, len(dp) == 2, that mean d[0] and dp[1] are valid, then d[2] create and error: out of index
        #to avoid this probem when n == 1 we immediately return dp[1]
        if (n == 1):
            return dp[1]

        dp[2] = 2; # based condition

        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2];
        return dp[n];
