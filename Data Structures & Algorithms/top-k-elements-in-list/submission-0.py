class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        num_count_map = {}
        freq = []
        output = []
        for n in nums:
            num_count_map[n] = num_count_map.get(n, 0) + 1
        for x, y in num_count_map.items():
            freq.append((y,x))
            freq = sorted(freq, key=lambda x: x[0])
            freq.reverse()
        for i in range(k):
            output.append(freq[i][1])
        return output
