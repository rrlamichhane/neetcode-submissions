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
        if len(s2) < len(s1):
            return False
        l, r = 0, len(s1)
        while r <= len(s2):
            cur_str = s2[l:r]
            print(l, r, cur_str)
            if self.checkPalindrome(s1, cur_str):
                return True
            l += 1
            r += 1
        return False
        