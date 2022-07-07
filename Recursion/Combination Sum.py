#{ 
#Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


 # } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,arr, B):
        
        arr = list(set(arr))
        arr.sort()
        
        res = []
        dp = {}
        def recurse(k1,arr1,amount):
            if amount > B:
                return
            if amount == B:
                res.append(arr1[:])
                return
            
            
            for i in range(k1,len(arr)):
                arr1.append(arr[i])
                recurse(i,arr1,amount+arr[i])
                arr1.pop()
        recurse(0,[],0)
        return(res)
    
        # code here

#{ 
#Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

#} Driver Code Ends
