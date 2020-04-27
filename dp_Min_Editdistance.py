# 可以根据当前两个位置上的元素是否一致，然后根据子串转换的最小编辑距离获得当前串转换需要的最小编辑距离
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1,1):
            dp[i][0] = i
        for j in range(1,m+1,1):
            dp[0][j] = j
        for i in range(1,n+1,1):
            for j in range(1,m+1,1):
                if word1[j-1] != word2[i-1]:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[n][m]
