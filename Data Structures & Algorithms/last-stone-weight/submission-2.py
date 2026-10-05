class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0]
        stoneheap = [-1 * x for x in stones]
        heapq.heapify(stoneheap)
        i, j = len(stones)-2, len(stones)-1
        while len(stoneheap) > 1:
            y = heapq.heappop(stoneheap)
            x = heapq.heappop(stoneheap)
            heapq.heappush(stoneheap, -1 * abs(x-y))
        return -1 * stoneheap[0]
