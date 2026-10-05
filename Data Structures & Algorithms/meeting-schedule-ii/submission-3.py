"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        et_heap = []
        heapq.heapify(et_heap)

        intervals.sort(key = lambda interval: interval.start)

        heapq.heappush(et_heap, intervals[0].end)
        for interval in intervals[1:]:
            s, e = interval.start, interval.end
            min_end = et_heap[0]
            if s >= min_end:
                heapq.heappop(et_heap)
            heapq.heappush(et_heap, e)
        
        return len(et_heap)
        