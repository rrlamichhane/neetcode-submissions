class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if i == j:
                    continue
                x, y = nums[i], nums[j]
                if x+y == target:
                    return [i,j]
        return []
