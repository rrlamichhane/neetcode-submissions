class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # idx, temp
        output = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                output[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, t))
        return output


    def dailyTemperatures_brute(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        evaluated_idx = {}
        for i in range(1, len(temperatures)):
            t_i = temperatures[i]
            for j in range(i):
                if j not in evaluated_idx:
                    t_j = temperatures[j]
                    if t_i > t_j:
                        evaluated_idx[j] = i - j
                        output[j] = i - j
        return output
