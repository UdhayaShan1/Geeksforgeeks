#User function Template for python3

class Solution:
    def permutation (self, S):
        # code here
        res = []
        def recurse(k1,arr1):
            if k1 >= len(S):
                res.append(' '.join(arr1))
                return
            
            
            for i in range(k1,len(S)):
                temp = S[k1:i+1]
                arr1.append(temp)
                recurse(i+1,arr1)
                arr1.pop()
        recurse(0,[])
        res.sort()
        return res
        pass




#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends
