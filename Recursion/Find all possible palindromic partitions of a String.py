#User function Template for python3

class Solution:
    def allPalindromicPerms(self, S):
        # code here 
        res = []
        def recurse(k1,arr1):
            if k1 >= len(S):
                res.append(arr1[:])
                return
            
            for i in range(k1,len(S)):
                temp = S[k1:i+1]
                if temp == temp[::-1]:
                    arr1.append(temp)
                    recurse(i+1,arr1)
                    arr1.pop()
        recurse(0,[])
        return(res)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends
