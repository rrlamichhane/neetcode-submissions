class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # idx, h
        max_area = float("-infinity")
        for i, h in enumerate(heights):
            start_idx = i
            while stack and h < stack[-1][1]:
                idx, old_h = stack.pop()
                popped_area = old_h * (i-idx)
                max_area = max(max_area, popped_area)
                start_idx = idx
            stack.append((start_idx, h))
        while stack:
            i, h = stack.pop()
            popped_area = (len(heights)-i) * h
            max_area = max(max_area, popped_area)
        return max_area    
        