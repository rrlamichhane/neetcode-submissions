class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                cur_sum = n + nums[l] + nums[r]
                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

    def threeSum_brute(self, nums: List[int]) -> List[List[int]]:
        zero_sums = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    triplets_sum = nums[i] + nums[j] + nums[k]
                    if triplets_sum == 0:
                        zero_sums.add((nums[i], nums[j], nums[k]))
        return [list(x) for x in zero_sums]
