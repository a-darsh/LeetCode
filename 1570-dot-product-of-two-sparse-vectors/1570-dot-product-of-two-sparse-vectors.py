class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []
        for i,val in enumerate(nums):
            if val:
                self.nums.append((i,val))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        i = j = 0
        while i<len(self.nums) and j<len(vec.nums):
            num1 = self.nums[i]
            num2 = vec.nums[j]
            if num1[0]==num2[0] and num1[1]:
                res+= num1[1]*num2[1]
                i+=1
                j+=1
            elif num1[0]<num2[0]:
                i+=1
            else:
                j+=1
        return res
            
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)