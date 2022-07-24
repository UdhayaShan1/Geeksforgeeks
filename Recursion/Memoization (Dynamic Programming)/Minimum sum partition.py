#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
        import sys
        dp = {}
        def dfs(k1,sum1,sum2):
            if k1 >= len(arr):
                return abs(sum1-sum2)
            if (k1,sum1,sum2) in dp:
                return dp[(k1,sum1,sum2)]
            
            incl_1 = dfs(k1+1,sum1+arr[k1],sum2)
            incl_2 = dfs(k1+1,sum1,sum2+arr[k1])
            dp[(k1,sum1,sum2)] = min(incl_1,incl_2)
            return min(incl_1,incl_2)
        return(dfs(0,0,0))
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends
