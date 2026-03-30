class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        start,end=intervals[0]
        merged=[]
        for i in range(1,len(intervals)):
            cur_start,cur_end=intervals[i]
            if cur_start<=end:
                end=max(end,cur_end)
            else:
                merged.append([start,end])
                start,end=cur_start,cur_end
        merged.append([start,end])
        return merged
                