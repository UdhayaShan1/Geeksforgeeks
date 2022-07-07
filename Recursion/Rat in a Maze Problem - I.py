#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        
        res = []
        dp2 = {}
        def dfs(i,j,arr1):
            if i >= len(m) or j >= len(m) or i < 0 or j < 0:
                return
            if m[i][j] == 0:
                return
            if i == len(m)-1 and j == len(m)-1:
                res.append(''.join(arr1[:]))
                return
            if (i,j) in dp2:
                return
            
            dp2[(i,j)] = 1
            arr1.append("D")
            y1 = dfs(i+1,j,arr1)
            
            arr1.pop()
            arr1.append("U")
            dp2[(i,j)] = 1
            y2 = dfs(i-1,j,arr1)
        
            arr1.pop()
            arr1.append("R")
            dp2[(i,j)] = 1
            y3 = dfs(i,j+1,arr1)
        
            arr1.pop()
            arr1.append("L")
            dp2[(i,j)] = 1
            y4 = dfs(i,j-1,arr1)
            arr1.pop()
            del dp2[(i,j)]
            
        dfs(0,0,[])
        return(res)
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends
