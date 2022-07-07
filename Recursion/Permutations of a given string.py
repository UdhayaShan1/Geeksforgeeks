#User function Template for python3

class Solution:
    def find_permutation(self, S):
        # Code here
        res = []
        def recurse(arr1,str1):
            if len(arr1) == len(S):
                res.append(''.join(arr1[:]))
                return
            
            for i in range(len(str1)):
                arr1.append(str1[i])
                recurse(arr1,str1[:i]+str1[i+1:])
                arr1.pop()
        recurse([],S)
        res = list(set(res))
        res.sort()
        return res
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        ob = Solution()
        ans = ob.find_permutation(S)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends
