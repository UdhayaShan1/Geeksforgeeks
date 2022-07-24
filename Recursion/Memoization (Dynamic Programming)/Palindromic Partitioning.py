#User function Template for python3

class Solution:
    def palindromicPartition(self, str1):
        # code here
        import sys
        dp = {}
        def dfs(k1):
            if k1 >= len(str1):
                return 0
            if k1 in dp:
                return dp[k1]
            y1 = sys.maxsize
            for i in range(k1,len(str1)):
                temp = str1[k1:i+1]
                if temp == temp[::-1]:
                    x=dfs(i+1)+1
                    y1 = min(x,y1)
            dp[k1] = y1
            return y1
        return(dfs(0)-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends
