class Solution:
    def isAnagram(self, s1, s2):
        if len(s1) != len(s2):
            return False
        char_dict = {}
        for c in s1:
            char_dict[c] = char_dict.get(c, 0) + 1
        for c in s2:
            if c not in char_dict:
                return False
            char_dict[c] = char_dict[c] - 1
            if char_dict[c] <= 0:
                del char_dict[c]
        if not char_dict:
            return True
        return False


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_strs = set()
        output = []
        if len(strs) == 1:
            return [strs]
        for i in range(len(strs)):
            s1 = strs[i]
            if s1 in grouped_strs:
                continue
            grouped_strs.add(s1)
            s_group = [s1]
            for j in range(i+1, len(strs)):
                s2 = strs[j]
                if self.isAnagram(s1, s2):
                    s_group.append(s2)
                    grouped_strs.add(s2)
            output.append(s_group)
        return output
