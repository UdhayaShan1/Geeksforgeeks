#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,str1,str2):
        
        # code here
        
        import sys
        dp = {}
        import functools
        @functools.lru_cache(None)
        def dfs(i,j):
            if i >= len(str1) or j >= len(str2):
                return 0
            
            if str1[i] == str2[j]:
                y1 = dfs(i+1,j+1)+1
                dp[(i,j)] = y1
            else:
                y1 = dfs(i+1,j)
                y2 = dfs(i,j+1)
                dp[(i,j)] = max(y1,y2)
            return dp[(i,j)]
        
        return(dfs(0,0))

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends
