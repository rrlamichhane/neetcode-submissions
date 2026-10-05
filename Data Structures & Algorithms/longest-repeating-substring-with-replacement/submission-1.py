class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_freq = 0
        char_cnt = {}
        left = 0
        for right in range(len(s)):
            char_cnt[s[right]] = char_cnt.get(s[right], 0) + 1
            max_freq = max(max_freq, char_cnt[s[right]])
            if right -left + 1 - max_freq > k:
                char_cnt[s[left]] -= 1
                left += 1
            max_len = max(right-left+1, max_len)
        return max_len
