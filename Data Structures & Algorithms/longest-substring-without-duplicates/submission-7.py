class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        start = 0
        last_seen = {}
        max_len = 0

        for i, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= start:
                start = last_seen[ch] + 1
            last_seen[ch] = i
            current_len = i - start + 1
            max_len = max(max_len, current_len)
        
        return max_len

            

        