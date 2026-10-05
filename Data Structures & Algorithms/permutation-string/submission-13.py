class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map, s2_map = {}, {}
        for i in range(ord('a'), ord('z')+1):
            s1_map[i] = 0
            s2_map[i] = 0
        
        for i, c in enumerate(s1):
            s1_map[ord(c)] += 1
            c2 = s2[i]
            s2_map[ord(c2)] += 1
        
        matches = 0
        for k, v in s1_map.items():
            if s2_map[k] == v:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            l_idx = ord(s2[l]) 
            if s1_map[l_idx] == s2_map[l_idx]:
                matches -= 1
            s2_map[l_idx] -= 1
            if s1_map[l_idx] == s2_map[l_idx]:
                matches += 1

            r_idx = ord(s2[r])
            if s1_map[r_idx] == s2_map[r_idx]:
                matches -= 1
            s2_map[r_idx] += 1
            if s1_map[r_idx] == s2_map[r_idx]:
                matches += 1
            
            l += 1
        
        return matches == 26
