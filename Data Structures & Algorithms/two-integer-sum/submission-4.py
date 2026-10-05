class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        offset_dict = {}
        for idx, n in enumerate(nums):
            if n in offset_dict:
                return [offset_dict[n], idx]
            offset_dict[target-n] = idx
        return False
        