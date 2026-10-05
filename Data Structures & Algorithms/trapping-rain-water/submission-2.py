from collections import namedtuple

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        acc_water = 0
        l, r = 0, len(height)-1
        l_max, r_max = 0, 0
        min_height = 0
        i = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            cur_water = 0
            for i in range(l, r):
                i_water = min(l_max, r_max) - max(height[i], min_height)
                if i_water > 0:
                    cur_water += i_water
            min_height = max(min(l_max, r_max), min_height)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            acc_water += cur_water
        return acc_water
