#User function Template for python3

class Solution:
    def numProvinces(self, nums, V):
        # code here 
        dp_tag = {}
        dp_visited = {}
        bruh = -1
        def dfs(city):
            if city in dp_visited:
                return
            if city in dp_tag:
                return
            dp_tag[city] = bruh
            for i in range(len(nums[city])):
                if nums[city][i] == 0 or i == city:
                    continue
                dp_visited[city] = 1
                y1 = dfs(i)

        
        
        for i in range(len(nums)):
            dfs(i)
            bruh-=1
        return(len(set(dp_tag.values())))

        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends
