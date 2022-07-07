#User function Template for python3

class Solution:
    def divAndSub(self, N):
        # code here 
        if N == 1:
            return "Arya"
        import math
        dp = {}
        def CanWin(N):
            if N == 1:
                return True
            if N == 0:
                return False
            if N in dp:
                return dp[N]
                
            for i in range(2,6):
                for j in ["/","-"]:
                    if j == "/":
                        y1 = CanWin(math.floor(N/i))
                        if not y1:
                            return True
                    else:
                        y1 = CanWin(N-i)
                        if not y1:
                            dp[N] = True
                            return True
            dp[N] = False
            return False
        
        x=(CanWin(N))
        if x == True:
            return "Jon"
        else:
            return "Arya"
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.divAndSub(N))
# } Driver Code Ends
