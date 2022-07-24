#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,N):
        
        # code here
        nums = [1,2,3]
        dp = {}
        import sys
        def dfs(length):
            if length == N:
                return 1
            if length > N:
                return 0
            if length in dp:
                return dp[length]
        
            y1 = 0
            for i in range(len(nums)):
                y1 += dfs(length+nums[i])
            dp[length] = y1
            return y1
        return(dfs(0)%1000000007)





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
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))
# } Driver Code Ends
