class Solution:
    def contains_substring(self, s:str, ss: str) -> bool:
        if len(s) < len(ss):
            return False
        t_chars = {}
        for c in ss:
            t_chars[c] = t_chars.get(c, 0) + 1
        for c in s:
            if c in t_chars:
                t_chars[c] -= 1
                if t_chars[c] == 0:
                    t_chars.pop(c)
        return not t_chars

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(s) == 0 or len(t) == 0:
            return ""
        cc_t, cc_win = {}, {}
        for c in t:
            cc_t[c] = cc_t.get(c, 0) + 1

        cc_have, cc_need = 0, len(cc_t)
        res, res_len = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            cc_win[c] = cc_win.get(c, 0) + 1

            if c in cc_t and cc_win[c] == cc_t[c]:
                cc_have += 1
            
            while cc_have == cc_need:
                cur_len = r - l + 1
                if cur_len < res_len:
                    res, res_len = [l, r], cur_len
                cl = s[l]
                cc_win[cl] -= 1
                if cl in cc_t and cc_win[cl] < cc_t[cl]:
                    cc_have -= 1
                l += 1
        return s[res[0]: res[1]+1] if res_len != float("infinity") else ""
