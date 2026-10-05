class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda pair: pair[0])
        pe = intervals[0][1]

        for s, e in intervals[1:]:
            if s < pe:
                ans += 1
                pe = min(e, pe)
            else:
                pe = e
        
        return ans
        