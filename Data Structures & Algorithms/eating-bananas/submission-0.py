class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        if h == len(piles):
            return max_pile
        l, r = 1, max_pile
        res = r

        while l <= r:
            k = (l + r) // 2
            cur_time = 0
            for p in piles:
                cur_time += math.ceil(float(p)/ k)
            if cur_time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
