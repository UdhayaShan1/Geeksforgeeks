#User function Template for python3

class Solution:
    def rremove (self, S):
        global res
        #code here
        res = ""
        def recurse(str1):
            global res
            #base conditions
            if len(str1) <= 1:
                res= str1
                return
            #base condition to check if string has any duplicates
            flag1 = 0
            for i in range(len(str1)-1):
                if str1[i] == str1[i+1]:
                    flag1+=1
                    break
            if flag1 == 0:
                res = str1
                return
            
            #remove duplicates and recur string
            str2 = ""
            flag = 0
            for i in range(len(str1)-1):
                if flag == 1:
                    if str1[i] == str1[i+1]:
                        flag=1
                    else:
                        flag=0
                    continue
                if str1[i] != str1[i+1]:
                    str2 += str1[i]
                else:
                    flag = 1
                    continue
            if str1[-1] != str1[-2]:
                str2 += str1[-1]
            recurse(str2)
        
        recurse(S)
        return(res)
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends
