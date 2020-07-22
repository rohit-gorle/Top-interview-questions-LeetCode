class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0]*(n+1)
        if n==1:
            return 1
        if n==2:
            return 2
        dp[1],dp[2] =1,2
        
        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
        
Second solution - for any given steps either 1 or 2 or 3:

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==0:
            return 1
        dp = [None]*(n+1)
        dp[0]= 1
        dp[1]= 1
        for i in range(2,n+1):
            result = 0
            for j in [1,2]:
                if i-j>=0:
                    result+=dp[i-j]
            dp[i]=result
        return dp[n]
