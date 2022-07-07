#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        global res
        #code here
        str1 = list(s)
        
        res = 0
        def recurse(str1,count,k1):
            global res
            res = max(res,int(''.join(str1)))
            if count == k or k1 >= len(str1):
                return
            
            
            
            if len(str1[k1+1:]) == 0:
                recurse(str1,count,k1+1)
            else:
                max1 = max(str1[k1+1:])
                if str1[k1] >= max1:
                    recurse(str1,count,k1+1)
                else:
                    for j in range(k1+1,len(str1)):
                        if str1[j] != max1:
                            continue
                        temp1 = str1[k1]
                        temp2 = str1[j]
                        str2 = str1[:]
                        str2[k1] = temp2
                        str2[j] = temp1
                        recurse(str2,count+1,k1+1)
        recurse(str1,0,0)
        return(res)
        
    




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob=Solution()
        print(ob.findMaximumNum(s,k))

# } Driver Code Ends
