class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtracking(idx, cur_combo, remain_target):
            if remain_target == 0:
                result.append(cur_combo[:])
                return
            
            for i in range(idx, len(candidates)):
                if candidates[i] > remain_target:
                    break
                
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                cur_combo.append(candidates[i])
                backtracking(i+1, cur_combo, remain_target-candidates[i])
                cur_combo.pop()

        
        backtracking(0, [], target)
        return result
