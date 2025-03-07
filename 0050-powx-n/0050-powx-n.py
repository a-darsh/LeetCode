class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            n=-1*n
            x=1/x
        res=1
        while n!=0:
            if n%2!=0:
                res*=x
                n-=1
            x=x*x
            n=n/2
        return res

        #O(logN), O(1)

            
