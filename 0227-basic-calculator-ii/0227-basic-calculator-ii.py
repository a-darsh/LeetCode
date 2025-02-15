class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        num = 0
        prev_op = '+'
        stack = []
        for i,c in enumerate(s):
            if c.isdigit():
                num  = num*10+int(c)
            if c in "+-/*" or i==len(s)-1:
                if prev_op=='+':
                    stack.append(num)
                elif prev_op=='-':
                    stack.append(-num)
                elif prev_op=='*':
                    prev_num = stack.pop()
                    stack.append(prev_num*num)
                else:
                    prev_num = stack.pop()
                    stack.append(int(prev_num/num))
                num=0
                prev_op=c
        return sum(stack)

        #O(N), O(N)



                