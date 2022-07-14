#User function Template for python3

class Solution:
    def AllParenthesis(self,n):
        #code here
        res = []
        def recurse(right,left,str1):
            if left > right:
                return
            if right == n and left == n:
                res.append(str1)
                return
            if right > n or left > n:
                return
            
            recurse(right+1,left,str1+"(")
            recurse(right,left+1,str1+")")
        
        recurse(0,0,"")
        return(list(set(res)))
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends
