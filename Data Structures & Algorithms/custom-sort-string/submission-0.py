class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_map = {c:i for (i,c) in enumerate(order)}
        print(char_map)
        suffix = ""
        prefix_idx = []
        order = []
        for c in s:
            if c not in char_map:
                suffix += c
            else:
                prefix_idx.append((char_map[c], c))
        prefix_idx.sort(key=lambda x: x[0])
        prefix = ""
        for i, c in prefix_idx:
            prefix += c
        return prefix + suffix
