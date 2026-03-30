class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
    
    # If total sum is odd, we can't partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
    
    # We are now looking for a subset with sum equal to total_sum // 2
        target_sum = total_sum // 2
        n = len(arr)
    
    # Initialize DP table
        dp = [[False for _ in range(target_sum + 1)] for _ in range(n + 1)]
    
    # It's always possible to have a subset with sum 0 (empty subset)
        for i in range(n + 1):
            dp[i][0] = True
    
    # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, target_sum + 1):
                if arr[i-1] > j:
                    dp[i][j] = dp[i-1][j]  # Exclude the element if it's larger than the target sum
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]  # Include or exclude the element

    # The answer will be in dp[n][target_sum]
        return dp[n][target_sum]
 # Output: True (The array can be partitioned into [1, 5, 5] and [11])

        