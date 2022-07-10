#User function Template for python3

class Solution:
    def arrayGame(self,N,A):
        #code here
        if len(set(A)) == 1:
            return "Draw"
        max1 = max(A)
        count = 0
        for i in A:
            if i == max1:
                continue
            count += (i-max1)
        if count % 2 == 0:
            return "Second"
        else:
            return "First"
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
    
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.arrayGame(N,A))
# } Driver Code Ends
