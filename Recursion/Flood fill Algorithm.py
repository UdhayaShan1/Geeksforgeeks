class Solution:
    def floodFill(self, image, sr, sc, newColor):
        #Code here
        og = image[sr][sc]
        dp2 = {}

        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
                return
            
            if image[i][j] != og:
                return
            if (i,j) in dp2:
                return
            
            image[i][j] = newColor
        
            
            dp2[(i,j)] = 1
            y1 = dfs(i+1,j)
            y2 = dfs(i,j+1)
            y3 = dfs(i-1,j)
            y4 = dfs(i,j-1)
            del dp2[(i,j)]
        
        dfs(sr,sc)
        return(image)

#{ 
#  Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

    T=int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        image = []
        for _ in range(n):
            image.append(list(map(int, input().split())))
        sr, sc, newColor = input().split()
        sr = int(sr); sc = int(sc); newColor = int(newColor);
        obj = Solution()
        ans = obj.floodFill(image, sr, sc, newColor)
        for _ in ans:
            for __ in _:
                print(__, end = " ")
            print()
# } Driver Code Ends
