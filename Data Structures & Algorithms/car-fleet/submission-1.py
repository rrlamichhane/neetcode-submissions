class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 0
        n = len(position)
        pos_time = [0] * n
        for i, p in enumerate(position):
            pos_time[i] = p, (target-p)/ speed[i]
            print(i, p, speed[i], pos_time[i])
        pos_time.sort(reverse=True)
        last_time = float("-infinity")
        print(pos_time)
        for p, t in pos_time:
            print(fleets, p, t, last_time)
            if t > last_time:
                fleets += 1
            last_time = max(t, last_time)
        return fleets
