class Solution:
    def maxCoins(self,Q, n):
        # Code here
        import functools
        @functools.lru_cache(None)
        def CanWin(A,i,j):
            if i > j:
                return 0
            if A == True:
                y1 = CanWin(False,i+1,j)+Q[i]
                y2 = CanWin(False,i,j-1)+Q[j]
                return max(y1,y2)
            else:
                y1 = CanWin(True,i+1,j)-Q[i]
                y2 = CanWin(True,i,j-1)-Q[j]
                return min(y1,y2)
        x=(CanWin(True,0,len(Q)-1))
        return (x+sum(Q))//2
           
#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends
