#Your Function should return a list containing all possible IP address
#No need to worry about order
class Solution:
    def genIp(self, S):
        #Code hereS = "55"
        S = str(S)
        res1 = []
        arr1 = []
        def recurse(k1):
            if k1 >= len(S):
                if len(arr1) != 4:
                    return
                res1.append('.'.join(arr1))
                return
            
            
            for i in range(k1,len(S)):
                temp = S[k1:i+1]
                if len(str(int(temp))) != len(temp) or int(temp) > 255:
                    continue
                arr1.append(temp)
                recurse(i+1)
                arr1.pop()
        
        (recurse(0))

        return(res1)
        

#{ 
#  Driver Code Starts
#Main
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().genIp(s)
        res.sort()
        if(len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
# } Driver Code Ends
