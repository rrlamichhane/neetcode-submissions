class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for str in strs:
            char_count_map = [0] * 26
            for c in str:
                char_count_map[ord(c)-ord('a')] += 1
            res[tuple(char_count_map)].append(str)
        
        return list(res.values())


        