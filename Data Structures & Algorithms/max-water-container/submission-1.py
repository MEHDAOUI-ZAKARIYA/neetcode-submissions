class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_water = 0
        while i < j :
            area  = (j - i) * min(heights[i] , heights[j])
            max_water = max (max_water , area)
            
            if heights[i] < heights[j] :
                i += 1
            else: j -= 1

        return max_water
            

        
                
            
                