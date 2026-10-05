class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in reversed(range(len(nums))):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
