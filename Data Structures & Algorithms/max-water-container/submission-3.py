class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights)-1
        
        while l < r:
            lh, rh = heights[l], heights[r]
            cur_water = min(lh, rh) * (r-l)
            max_water = max(max_water, cur_water)
            if rh > lh:
                l += 1
            else:
                r -= 1
        
        return max_water