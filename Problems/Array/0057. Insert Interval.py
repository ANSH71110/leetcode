class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        intervals.append(newInterval)
        intervals.sort()
        while i<len(intervals)-1:
            if intervals[i][-1]>=intervals[i+1][0]:
                intervals[i][0]=min(intervals[i][0],intervals[i+1][0])
                intervals[i][-1]=max(intervals[i+1][-1],intervals[i][-1])
                intervals.pop(i+1)
                i-=1
            i+=1
        return intervals
