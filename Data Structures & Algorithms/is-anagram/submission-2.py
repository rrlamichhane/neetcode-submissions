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
            char_dict[c] = char_dict[c] - 1
            if char_dict[c] == 0:
                del char_dict[c]
        return not char_dict
        