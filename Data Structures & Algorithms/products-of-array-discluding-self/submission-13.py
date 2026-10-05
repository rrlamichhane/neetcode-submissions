class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for l in range(len(nums)):
            res[l] = prefix
            prefix *= nums[l]
        
        postfix = 1
        for r in reversed(range(len(nums))):
            res[r] *= postfix
            postfix *= nums[r]

        return res
        