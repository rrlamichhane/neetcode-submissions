class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_map = {}
        for c in s1:
            char_map[c] = char_map.get(c, 0) + 1
        
        cur_map = char_map.copy()
        first_char_idx = 0
        for i, c in enumerate(s2):
            if c in cur_map:
                if cur_map[c] == 1:
                    print(cur_map, c)
                    del cur_map[c]
                    if not cur_map:
                        return True
                else:
                    cur_map[c] = cur_map[c] - 1
            elif c in char_map and c == s2[first_char_idx]:
                first_char_idx += 1
            else:
                cur_map = char_map.copy()
                first_char_idx = i
        
        if cur_map:
            return False

