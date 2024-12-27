class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hmap = {}
        for i,num in enumerate(numbers):
            rem = target-num
            if rem in hmap:
                return [hmap[rem], i+1]
            hmap[num]=i+1
        