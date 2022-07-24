#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
		# Code here

        
        import functools
        @functools.lru_cache(None)
        def dfs(increase,k1,prev):
        
            if k1 >= len(nums):
                return 0
            
            
            if increase == True:
                if prev == -1:
                    y1 = dfs(True,k1+1,nums[k1])+1
                    y2 = dfs(False,k1+1,nums[k1])+1
                    y3 = dfs(True,k1+1,prev)
                    return max(y1,y2,y3)
                else:
                    if nums[k1] > prev:
                        y1 = dfs(True,k1+1,nums[k1])+1
                        y2 = dfs(False,k1+1,nums[k1])+1
                        y3 = dfs(True,k1+1,prev)
                        y4 = dfs(False,k1+1,prev)
                        return max(y1,y2,y3,y4)
                    else:
                        y1 = dfs(True,k1+1,prev)
                        y2 = dfs(False,k1+1,prev)
                        return max(y1,y2)
        
            else:
                if nums[k1] < prev:
                    y1 = dfs(False,k1+1,nums[k1])+1
                    y2 = dfs(False,k1+1,prev)
                    return max(y1,y2)
                else:
                    y1 = dfs(False,k1+1,prev)
                    return y1
            
        return(dfs(True,0,-1))
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends
