class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key = lambda pair: pair[0])
        ps, pe = intervals[0]

        for s, e in intervals[1:]:
            if s < pe:
                ans += 1
                ps, pe = s, min(e, pe)
            else:
                ps, pe = s, e
        
        return ans
        