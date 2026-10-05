class Solution:
    def checkPalindrome(self, s1: str, s2: str) -> bool:
        char_count = {}
        for c in s1:
            char_count[c] = char_count.get(c, 0) + 1
        for c in s2:
            if c not in char_count:
                return False
            char_count[c] -= 1
            if char_count[c] == 0:
                char_count.pop(c)
        return not char_count

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_chars = [0] * 26
        s2_chars = [0] * 26
        for i in range(len(s1)):
            s1_chars[ord(s1[i]) - ord("a")] += 1
            s2_chars[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1_chars[i] == s2_chars[i] else 0
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord("a")
            s2_chars[idx] += 1
            if s1_chars[idx] == s2_chars[idx]:
                matches += 1
            elif s1_chars[idx] + 1 == s2_chars[idx]:
                matches -= 1
            
            idx = ord(s2[l]) - ord("a")
            s2_chars[idx] -= 1
            if s1_chars[idx] == s2_chars[idx]:
                matches += 1
            elif s1_chars[idx] - 1 == s2_chars[idx]:
                matches -= 1
            l += 1
        return matches == 26


    def checkInclusion_dict(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1)
        while r <= len(s2):
            cur_str = s2[l:r]
            if self.checkPalindrome(s1, cur_str):
                return True
            l += 1
            r += 1
        return False
        