# User function Template for Python3

class Solution:
    def minThrow(self, N, arr):
        # code here
               
        ladder = {}
        snakes = {}
        for i in range(0,len(arr),2):
            if arr[i] < arr[i+1]:
                ladder[arr[i]] = arr[i+1]

        for i in range(0,len(arr),2):
            if arr[i] > arr[i+1]:
                snakes[arr[i]] = arr[i+1]

        
        import sys
        dp = {}
        dp2 = {} #set to track visited cells
        import functools
        @functools.lru_cache(None)
        def dfs(k1):
        
            if k1 == 30:
                return 0
            if k1 in dp2 or k1 > 30:
                return sys.maxsize
            
            if k1 in ladder:
                dp2[k1] = 1
                y1 = dfs(ladder[k1])
                del dp2[k1]
            elif k1 in snakes:
                dp2[k1] = 1
                y1 = dfs(snakes[k1])
                del dp2[k1]
            else:
                y1 = sys.maxsize
                for i in range(1,7):
                    dp2[k1] = 1
                    x = dfs(k1+i)+1
                    del dp2[k1]
                    y1 = min(x,y1)
            return y1
        return(dfs(1))
        


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(2*N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.minThrow(N, arr))
# } Driver Code Ends
