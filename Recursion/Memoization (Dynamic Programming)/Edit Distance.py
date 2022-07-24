class Solution:
	def editDistance(self, s, t):
		# Code here
        
        import sys
        dp = {}
        import functools
        @functools.lru_cache(None)
        def dfs(i,j):
            if i >= len(s):
                return len(t)-j
            if j >= len(t):
                return len(s)-i
            
            
            if s[i] == t[j]:
                y1 = dfs(i+1,j+1)
                return y1
            else:
                y1 = dfs(i+1,j)+1
                y2 = dfs(i+1,j+1)+1
                y3 = dfs(i,j+1)+1
                return min(y1,y2,y3)
        return(dfs(0,0))

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution();
		ans = ob.editDistance(s, t)
		print(ans)
# } Driver Code Ends
