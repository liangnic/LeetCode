class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        boundNum = [1]+nums+[1]
        
        length = len(nums)
        dp = [[0]*(length+2) for _ in range(length+2)]
        
        for i in range(length-1, -1, -1):
            for j in range(i + 2, length + 2):
                for k in range(i + 1, j):
                    total = boundNum[i]*boundNum[k]*boundNum[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)
        
        return dp[0][length+1]