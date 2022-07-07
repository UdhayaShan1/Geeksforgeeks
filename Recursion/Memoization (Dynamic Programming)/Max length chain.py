#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''

def maxChainLen(P, n):
    # Parr:  list of pair
    #code here

    
    import sys
    dp = {}
    dp2 = {}
    def dfs(k1,prev):
        if k1 >= len(P):
            return 0
        
        if (k1,prev) in dp:
            return dp[(k1,prev)]
        
        
        if prev == -1:
            dp2[k1] = 1
            y1 = dfs(0,P[k1].b)+1
            del dp2[k1]
            y2 = dfs(k1+1,prev)
            dp[(k1,prev)] = max(y1,y2)
        else:
            if P[k1].a > prev and k1 not in dp2:
                dp2[k1] = 1
                y1 = dfs(0,P[k1].b)+1
                del dp2[k1]
                y2 = dfs(k1+1,prev)
                dp[(k1,prev)] = max(y1,y2)
            else:
                y1 = dfs(k1+1,prev)
                dp[(k1,prev)] = y1
        return dp[(k1,prev)]
        
    return(dfs(0,-1))


#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))

        print(maxChainLen(Parr, n))
# } Driver Code Ends
