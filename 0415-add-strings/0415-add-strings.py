class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        res = []
        p1, p2 = len(num1)-1, len(num2)-1
        change = 0
        while p1>=0 or p2>=0:
            x1 = ord(num1[p1])-ord('0') if p1>=0 else 0
            x2 = ord(num2[p2])-ord('0') if p2>=0 else 0
            value = (x1+x2+change)%10
            change = (x1+x2+change)//10
            res.append(value)
            p1-=1
            p2-=1
        if change>0:
            res.append(change)
        return ''.join(str(x) for x in res[::-1])

        #O(max(N,M)), O(max(N,M))
