class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums)
        maxString = '1'*l
        num = int(maxString,2)
        
        while True:
            temp = f"{bin(num)[2:]:0{l}}"
            if temp not in nums:
                return temp
            num -= 1
        