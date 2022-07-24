#User function Template for python3
class Solution:
	def NBitBinary(self, N):
		# code here
        res = []
        def dfs(arr1,ones,zero):
            if len(arr1) == N:
                res.append(''.join(arr1))
                return
            
            
            if zero == ones:
                arr1.append("1")
                dfs(arr1,ones+1,zero)
                arr1.pop()
            if ones > zero:
                arr1.append("0")
                dfs(arr1,ones,zero+1)
                arr1.pop()
                
                arr1.append("1")
                dfs(arr1,ones+1,zero)
                arr1.pop()
        
        dfs([],0,0)
        res.sort()
        res = res[::-1]
        return(res)
            
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends
