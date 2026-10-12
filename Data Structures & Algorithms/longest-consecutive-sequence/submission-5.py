class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        dict = {}
        if not nums:
            return 0
        for i in range(len(nums)):
              if nums[i] -1 not in dict:
                    dict[nums[i]] = 1
              else:
                    dict[nums[i]] = dict[nums[i]-1] + 1
        return max(dict.values())

    