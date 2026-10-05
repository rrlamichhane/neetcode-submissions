class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zero_sums = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    print(i, j, k)
                    triplets_sum = nums[i] + nums[j] + nums[k]
                    if triplets_sum == 0:
                        triplets = sorted([nums[i], nums[j], nums[k]])
                        if triplets not in zero_sums:
                            zero_sums.append(triplets)
        return zero_sums

