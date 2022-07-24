# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        
        dp2 = {}
        import functools
        @functools.lru_cache(None)
        def dfs(i,j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return 0
            if (i,j) in dp2:
                return 0
            dp2[(i,j)] = 1
            y1 = dfs(i-1,j+1)+M[i][j]
            y2 = dfs(i,j+1)+M[i][j]
            y3 = dfs(i+1,j+1)+M[i][j]
            del dp2[(i,j)]
            return max(y1,y2,y3)
        
        max1 = 0
        for i in range(n):
            max1 = max(max1,dfs(i,0))
        return max1
    


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends
