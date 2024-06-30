class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        if len(A) > len(B):
            A,B = B,A
        
        total = len(A)+len(B)
        half = total//2
        
        l,r = 0, len(A)-1
        while True:
            i = (l+r)//2
            j = half-i-2
            
            Aleft = A[i] if i>=0 else float('-inf')
            Aright = A[i+1] if (i+1)<len(A) else float('inf')
            Bleft = B[j] if j>=0 else float('-inf')
            Bright = B[j+1] if (j+1)<len(B) else float('inf')
            
            if Aleft<= Bright and Bleft <= Aright:
                if total%2:
                    return min(Aright, Bright)
                else:
                    t1 = max(Aleft, Bleft)
                    t2 = min(Aright, Bright)
                    return (t1+t2)/2
            
            elif Aleft>Bright:
                r = i-1
            else:
                l = i+1
        