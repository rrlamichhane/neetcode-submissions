class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        max_len = 0

        for i, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1
            last[c] = i
            max_len = max(max_len, i- left + 1)
        
        return max_len
