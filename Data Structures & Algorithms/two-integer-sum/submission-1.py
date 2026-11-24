class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      seen = {}

      for i,item in enumerate(nums) :
        
        complement = target - item 

        if complement in seen :
            return [seen[complement] , i ]
        
        seen[item] = i