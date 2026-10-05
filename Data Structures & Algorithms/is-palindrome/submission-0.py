class Solution:
    def is_alpha_numeric(self, c: str) -> bool:
        if c.isalpha() or c.isnumeric():
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            sl, sr = s[i].lower(), s[j].lower()
            if not self.is_alpha_numeric(sl):
                i += 1
                continue
            if not self.is_alpha_numeric(sr):
                j -= 1
                continue
            if sl == sr:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
