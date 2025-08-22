class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = height[0], height[-1]
        l,r = 0, len(height)-1
        res = 0
        while l<r:
            if height[l]<height[r]:
                if height[l]>=leftMax:
                    leftMax = height[l]
                else:
                    res+= (leftMax-height[l])
                l+=1
            else:
                if height[r]>=rightMax:
                    rightMax = height[r]
                else:
                    res+=(rightMax-height[r])
                r-=1
        return res
                