class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        mid = n// 2
        count = 0
        while mid < n:
            count += 1
            if count == 10:
                break
            print(l, r, mid, nums[mid], target)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
                mid += max((r - l) // 2, 1)
            else:
                r = mid
                mid = mid// 2
        return -1
        