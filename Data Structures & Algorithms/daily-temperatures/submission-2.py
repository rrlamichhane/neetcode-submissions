class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                st_t, st_i = stack.pop()
                res[st_i] = i - st_i
            
            stack.append((t, i))
        
        return res
        