#User function Template for python3

class Solution:
    def count(self, S, m, n): 
        # code here 
        S.insert(0,0)
        S.sort()
        
        dp = {}
        for i in range(len(S)):
            dp[i] = []
            for j in range(1,n+1):
                dp[i].append(0)
        
        
        for i in range(len(S)):
            if i == 0:
                continue
            for j in range(n):
                if j+1 < S[i]:
                    dp[i][j] = dp[i-1][j]
                elif j+1 == S[i]:
                    dp[i][j] = 1+dp[i-1][j]
                else:
                    remain = j+1-S[i]
                    if dp[i][remain-1] > 0:
                        dp[i][j] = dp[i][remain-1]+dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
        return(dp[len(S)-1][n-1])
                



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends
