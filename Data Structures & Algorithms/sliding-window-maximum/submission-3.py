from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        res = []
        sublist = deque()
        for r in range (len(nums)) :

            while sublist and nums[sublist[-1]] < nums[r]:
                sublist.pop()

            sublist.append(r)

            if sublist[0] < l:
                sublist.popleft()

            if r - l + 1 == k : 
                res.append(nums[sublist[0]])
                l += 1
        return res 



             