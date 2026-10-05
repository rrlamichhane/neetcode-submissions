class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for x in nums:
            nums_map[x] = nums_map.get(x, 0) + 1
            if nums_map[x] > 1:
                return True
        return False
