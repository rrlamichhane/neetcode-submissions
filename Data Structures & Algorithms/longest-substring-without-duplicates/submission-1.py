class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        char_set = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len


    def lengthOfLongestSubstring_brute(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 0
        for i in range(len(s)):
            cur_str = s[i]
            for j in range(i+1, len(s)):
                if s[j] in cur_str:
                    break
                cur_str += s[j]
            max_len = max(max_len, len(cur_str))
        return max_len
        