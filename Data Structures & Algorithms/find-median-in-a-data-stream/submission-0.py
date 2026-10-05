class MedianFinder:

    def __init__(self):
        self.minh_right = []
        self.maxh_left = []
    
    def addNum(self, num: int) -> None:
        if self.minh_right and num > self.minh_right[0]:
            heapq.heappush(self.minh_right, num)
        else:
            heapq.heappush(self.maxh_left, -1 * num)
        if len(self.maxh_left) > len(self.minh_right) + 1:
            val = -1 * heapq.heappop(self.maxh_left)
            heapq.heappush(self.minh_right, val)
        if len(self.minh_right) > len(self.maxh_left) + 1:
            val = heapq.heappop(self.minh_right)
            heapq.heappush(self.maxh_left, -1 * val)

    def findMedian(self) -> float:
        if len(self.maxh_left) > len(self.minh_right):
            return -1 * self.maxh_left[0]
        elif len(self.minh_right) > len(self.maxh_left):
            return self.minh_right[0]
        return (-1 * self.maxh_left[0] + self.minh_right[0]) / 2.0
