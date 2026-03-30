class Solution:
    def climbStairs(self, n: int) -> int:
        def CS(ind: int,dp: List[int])->int:
            
            if ind<=1:return 1
            if dp[ind]!=-1:
                return dp[ind]
            left=CS(ind-1,dp)
            
            right=CS(ind-2,dp)
            dp[ind]=left+right
            return dp[ind]
        dp=(n+1)*[-1]
        return CS(n,dp)

        