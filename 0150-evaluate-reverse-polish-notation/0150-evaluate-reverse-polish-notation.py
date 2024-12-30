class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []
        for t in tokens:
            if t in ["+","-","*","/"]:
                a = stck.pop()
                b = stck.pop()
                if t=="+":
                    stck.append(b+a)
                elif t=="-":
                    stck.append(b-a)
                elif t=="*":
                    stck.append(a*b)
                else:
                    stck.append(int(b/a))
            else:
                stck.append(int(t))
        
        return stck.pop()