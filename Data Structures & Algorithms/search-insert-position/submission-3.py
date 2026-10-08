class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if target < nums[l]:
            return 0
        if target > nums[r]:
            return r + 1
        
        while l <= r:
            m = l + ( r - l ) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return l
