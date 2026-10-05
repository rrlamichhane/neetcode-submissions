class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zero_sums = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    triplets_sum = nums[i] + nums[j] + nums[k]
                    if triplets_sum == 0:
                        zero_sums.add((nums[i], nums[j], nums[k]))
        return [list(x) for x in zero_sums]
