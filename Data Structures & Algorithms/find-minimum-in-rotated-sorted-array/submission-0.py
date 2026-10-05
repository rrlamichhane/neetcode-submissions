class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_n = float("+infinity")
        while l <= r:
            m = l + ((r - l)// 2)
            min_n = min(min_n, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return min(min_n, nums[l])
        