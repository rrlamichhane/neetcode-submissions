class Solution:
    def __init__(self):
        self.separator = "~#!-"

    def encode(self, strs: List[str]) -> str:
        res = self.separator
        n = len(strs)
        res += str(n) + self.separator
        for s in strs:
            sl = len(s)
            res += str(sl) + self.separator + s + self.separator
        return res

    def decode(self, s: str) -> List[str]:
        sep_len = len(self.separator)
        i = sep_len
        j = s.find(self.separator, i)
        num_strs = int(s[i:j])
        i = j + sep_len

        ans = []

        for _ in range(num_strs):
            j = s.find(self.separator, i)
            str_len = int(s[i:j])
            i = j + sep_len
            ans.append(s[i:i+str_len])

            i+= str_len + sep_len
        return ans
