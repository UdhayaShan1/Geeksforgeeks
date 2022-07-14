#User function Template for python3

class Solution:
    def findMinInsertions(self, s):
        # code here
        import sys
        dp = {}
        import functools
        sys.setrecursionlimit(10**7)

        def dfs(i,j):
            if i >= j:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if s[i] != s[j]:
                y1 = dfs(i+1,j)+1
                y2 = dfs(i,j-1)+1
                dp[(i,j)] = min(y1,y2)
            else:
                y1 = dfs(i+1,j-1)
                dp[(i,j)] = y1
            return dp[(i,j)]
        
        return(dfs(0,len(s)-1))
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.findMinInsertions(S))
# } Driver Code Ends
