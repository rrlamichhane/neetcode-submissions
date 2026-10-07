class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {(target-x): i for (i, x) in enumerate(nums)}
        for idx, n in enumerate(nums):
            if n in target_map:
                j = target_map[n]
                if idx != j:
                    return [idx, j]
