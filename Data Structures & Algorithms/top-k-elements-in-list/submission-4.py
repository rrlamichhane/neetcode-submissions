import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        num_freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1
        for num, cnt in num_count.items():
            num_freq[cnt].append(num)
        
        res = []
        for r_idx in reversed(range(len(num_freq))):
            for n in num_freq[r_idx]:
                res.append(n)
                if len(res) == k:
                    return res
        return False



