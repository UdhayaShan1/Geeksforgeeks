#User function Template for python3

class Solution:
	def all_longest_common_subsequences(self, s, t):
		# Code here
        import sys
        dp = {}
        import functools
        @functools.lru_cache(None)
        def dfs(i,j):
            if i >= len(s) or j >= len(t):
                return 0
            
            if s[i] == t[j]:
                y1 = dfs(i+1,j+1)+1
                return y1
            else:
                y1 = dfs(i+1,j)
                y2 = dfs(i,j+1)
                return max(y1,y2)
        
        x=(dfs(0,0))
        
        
        res = []
        @functools.lru_cache(None)
        def dfs2(i,j,str1):
            if i >= len(s) or j >= len(t):
                if len(str1) == x:
                    res.append(str1)
                return 0
            
            if s[i] == t[j]:
                y1 = dfs2(i+1,j+1,str1+s[i])+1
                y2 = dfs2(i+1,j+1,str1+t[j])+1
                return max(y1,y2)
            else:
                y1 = dfs2(i+1,j,str1)
                y2 = dfs2(i,j+1,str1)
                return max(y1,y2)
        
        dfs2(0,0,"")
        y=(list(set(res)))
        y.sort()
        return y



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s, t = input().split()
		ob = Solution()
		ans = ob.all_longest_common_subsequences(s, t)
		for i in ans:
			print(i, end = " ")
		print()




# } Driver Code Ends
