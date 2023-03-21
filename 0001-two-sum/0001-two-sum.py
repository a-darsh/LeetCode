class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}
        for i,val in enumerate(nums):
          if target-val in sum_dict:
            return [sum_dict[target-val],i]
          sum_dict[val] = i