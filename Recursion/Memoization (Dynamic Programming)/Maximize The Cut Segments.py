#User function Template for python3


class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,N,x,y,z):
        #code here
        arr = [x,y,z]
        arr.sort()
        
        dp = {}
        for i in range(4):
            dp[i] = []
            for j in range(N+1):
                dp[i].append(0)
        
        for i in range(1,len(arr)+1):
            for j in range(1,N+1):
                if j < arr[i-1]:
                    dp[i][j] = dp[i-1][j]
                elif j == arr[i-1]:
                    dp[i][j] = max(1,dp[i-1][j])
                else:
                    remain = j-arr[i-1]
                    if dp[i][remain] > 0:
                        dp[i][j] = max(1+dp[i][remain],dp[i-1][j])
                    else:
                        dp[i][j] = dp[i-1][j]
        return(dp[len(arr)][N])
        
    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends
