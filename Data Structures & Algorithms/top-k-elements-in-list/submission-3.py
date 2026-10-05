import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_d = {}
        minheap = []
        heapq.heapify(minheap)
        for n in nums:
            nums_d[n] = nums_d.get(n, 0) + 1
        for n in nums_d.keys():
            freq = nums_d[n]
            if len(minheap) < k:
                heapq.heappush(minheap, (freq, n))
                continue
            smallest = heapq.nsmallest(1, minheap)[0][0]
            if smallest < freq:
                heapq.heappush(minheap, (freq, n))
                heapq.heappop(minheap)
        
        return [x[1] for x in list(minheap)]