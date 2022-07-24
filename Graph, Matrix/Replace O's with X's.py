#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        # code here
        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
                return
            if mat[i][j] == "X":
                return
            if (i,j) in dp2:
                return
            if mat[i][j] == "O":
                mat[i][j] = "1"
            dp2[(i,j)] = 1
            y1 = dfs(i+1,j)
            y2 = dfs(i,j+1)
            y3 = dfs(i-1,j)
            y4 = dfs(i,j-1)
            del dp2[(i,j)]
        
        dp2 = {}
        for i in [0,n-1]:
            for j in range(m):
                if mat[i][j] == "O":
                    mat[i][j] = "1"
                    dfs(i,j)
        
        for j in [0,m-1]:
            for i in range(n):
                if mat[i][j] == "O":
                    mat[i][j] = "1"
                    dfs(i,j)

        for i in range(n):
            for j in range(m):
                if mat[i][j] == "O":
                    mat[i][j] = "X"
                elif mat[i][j] == "1":
                    mat[i][j] = "O"


        return(mat)
            
            
            
    
    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends
