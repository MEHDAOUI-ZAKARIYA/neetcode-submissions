class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort()

        # j = 0

        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= intervals[j][1]:
        #         intervals[j][1] = max(intervals[j][1], intervals[i][1])
        #     else:
        #         j += 1
        #         intervals[j] = intervals[i]

        # return intervals[:j+1]

        intervals.sort(key = lambda  x : x[0])

        merged = []

        for interval in intervals  :
            if not merged or merged[-1][1] < interval[0] :
                merged.append(interval)
            else :
                merged[-1] = [merged[-1][0] , max(merged[-1][1] , interval[1])]
        
        return merged 



