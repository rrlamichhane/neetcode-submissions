import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points
        distances = [(-1 * math.sqrt(p[0]**2 + p[1]**2), p) for p in points]
        # distance_map = {math.sqrt(p[0]**2 + p[1]**2): p for p in points}
        # distances = [-d for d in distance_map.keys()]
        print(distances)
        heapq.heapify(distances)
        while len(distances) > k:
            heapq.heappop(distances)
        return [p[1] for p in distances]
        