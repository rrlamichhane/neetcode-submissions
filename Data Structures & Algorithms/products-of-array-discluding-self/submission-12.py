class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = suffix = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for j in reversed(range(len(nums))):
            res[j] *= suffix
            suffix *= nums[j]

        return res
        