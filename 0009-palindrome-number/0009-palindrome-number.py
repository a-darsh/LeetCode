class Solution:
    def isPalindrome(self, x: int) -> bool:
        # temp = str(x)
        # i,j = 0,len(temp)-1
        # while(i<j):
        #     if temp[i]!=temp[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True
        
        if x<0 or x%10==0 and x!=0:
            return False
        
        revX = 0
        temp = x
        while revX<temp:
            revX = revX*10 + temp%10
            temp = temp//10
        
        return revX==temp or (revX//10)==temp
            
            
        