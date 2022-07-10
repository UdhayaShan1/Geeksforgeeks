#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, weight1, values, n):
       
        # code hereN = 3
        
        import sys
        import functools
        dp = {}
        def dfs(k1,weight):
            if weight > W:
                return -sys.maxsize
            if k1 >= len(values):
                return 0
            if (k1,weight) in dp:
                return dp[(k1,weight)]
            
            y1 = dfs(k1+1,weight+weight1[k1])+values[k1]
            y2 = dfs(k1+1,weight)
            dp[(k1,weight)] = max(y1,y2)
            return max(y1,y2)
        return(dfs(0,0))
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
