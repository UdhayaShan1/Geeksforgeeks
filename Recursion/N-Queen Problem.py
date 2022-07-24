#User function Template for python3

class Solution:
    def nQueen(self, N):
        # code here
        nums = []
        for i in range(N):
            nums.append([])
            for j in range(N):
                nums[i].append("0")
        
        import copy
        res = []
        def dfs(k1,nums):
            if k1 >= N:
                tmp = []
                for i in range(N):
                    for j in range(N):
                        if nums[i][j] == "Q":
                            tmp.append(j+1)
                res.append(tmp)
                return
            
            
            
            for col in range(N):
                if nums[k1][col] == "X":
                    continue
                nums2 = copy.deepcopy(nums)
                nums2[k1][col] = "Q"
                
                for k in range(N):
                    nums2[k][col] = "X"
                
                for k in range(N):
                    nums2[k1][k] = "X"
                
                
                dp2 = {}
                def dfs1(i,j):
                    if i < 0 or j < 0 or i >= N or j >= N:
                        return
                    if (i,j) in dp2:
                        return
                    nums2[i][j] = "X"
                    
                    dp2[(i,j)] = 1
                    y1 = dfs1(i+1,j+1)
                    y2 = dfs1(i-1,j-1)
                    del dp2[(i,j)]
                dfs1(k1,col)
                
                
                dp2 = {}
                def dfs2(i,j):
                    if i < 0 or j < 0 or i >= N or j >= N:
                        return
                    if (i,j) in dp2:
                        return
                    nums2[i][j] = "X"
                    
                    dp2[(i,j)] = 1
                    y1 = dfs2(i-1,j+1)
                    y2 = dfs2(i+1,j-1)
                    del dp2[(i,j)]
                dfs2(k1,col)
                nums2[k1][col] = "Q"
                
                dfs(k1+1,nums2)
        dfs(0,nums)
        return res
        
        
        
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends
