class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = {}
        for c in s:
            char_dict[c] = char_dict.get(c, 0) + 1
        for c in t:
            if c not in char_dict:
                return False
            if char_dict[c] == 1:
                char_dict.pop(c)
                continue
            char_dict[c] -= 1
        if char_dict:
            return False
        return True
