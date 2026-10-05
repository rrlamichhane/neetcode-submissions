class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            cur_str = s[i]
            for j in range(i+1, len(s)):
                if s[j] in cur_str:
                    break
                cur_str += s[j]
            max_len = max(max_len, len(cur_str))
        return max_len
        