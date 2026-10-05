from collections import namedtuple

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        right_max[n-1] = height[n-1]

        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
        
        for i in reversed(range(n-1)):
            right_max[i] = max(height[i], right_max[i+1])
        
        acc_water = 0
        for i in range(n):
            acc_water += min(left_max[i], right_max[i]) - height[i]
    
        return acc_water



    def trap_brute(self, height: List[int]) -> int:
        if not height:
            return 0
        lmax, rmax = 0, 0
        acc_water = 0
        for i in range(len(height)):
            lmax = rmax = height[i]
            for j in range(i):
                lmax = max(lmax, height[j])
            for j in range(i+1, len(height)):
                rmax = max(rmax, height[j])
            acc_water += min(lmax, rmax) - height[i]
        return acc_water
            
    
    def trap_orig(self, height: List[int]) -> int:
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
