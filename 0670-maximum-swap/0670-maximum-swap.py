class Solution:
    def maximumSwap(self, num: int) -> int:
        maxDigit = "0"
        num = list(str(num))
        maxInd =-1
        swapI = swapJ = -1
        for i in range(len(num)-1, -1, -1):
            if num[i]>maxDigit:
                maxDigit = num[i]
                maxInd = i
            if num[i]<maxDigit:
                swapI, swapJ = i, maxInd
        num[swapI], num[swapJ] = num[swapJ], num[swapI]
        return int(''.join(num))


