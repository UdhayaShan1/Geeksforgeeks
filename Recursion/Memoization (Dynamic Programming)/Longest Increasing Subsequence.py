#User function Template for python3

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,A,n):
        # code here
        
        import sys
        dp = {}
        import functools
        @functools.lru_cache(None)
        def dfs(k1,prev):
            if k1 >= len(A):
                return 0
            
            if prev == -1:
                y1 = dfs(k1+1,prev)
                y2 = dfs(k1+1,A[k1])+1
                dp[(k1,prev)] = max(y1,y2)
            else:
                if A[k1] > prev:
                    y1 = dfs(k1+1,prev)
                    y2 = dfs(k1+1,A[k1])+1
                    dp[(k1,prev)] = max(y1,y2)
                else:
                    y1 = dfs(k1+1,prev)
                    dp[(k1,prev)] = y1
            return dp[(k1,prev)]
        
        return(dfs(0,-1))
    

       


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends
