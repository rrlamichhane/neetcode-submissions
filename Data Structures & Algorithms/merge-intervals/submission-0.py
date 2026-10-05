class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for interval in intervals:
            s, e = interval
            if s > merged[-1][1]:
                merged.append([s, e])
                continue
            merged[-1][0], merged[-1][1] = min(merged[-1][0], s), max(merged[-1][1], e)
        
        return merged
