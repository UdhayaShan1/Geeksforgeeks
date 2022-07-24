#User function Template for python3

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        if len(a) == 1:
            return a[0]
        if len(a) == 2:
            return max(a[0],a[1])
        if len(a) == 3:
            return max(a[1],a[2]+a[0])
        # code here
        dp = {}
        dp[0] = a[0]
        dp[1] = a[1]
        dp[2] = max(a[1],a[2]+a[0])
        for i in range(3,len(a)):
            dp[i] = a[i]+max(dp[i-2],dp[i-3])
        return(max(dp.values()))


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.FindMaxSum(a,n))
# } Driver Code Ends
