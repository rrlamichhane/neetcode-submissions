class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        product = 1
        num_zeroes = 0
        for i in nums:
            if i == 0:
                num_zeroes += 1
            else:
                product *= i
            if num_zeroes > 1:
                return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                output[i] = product
            elif num_zeroes == 1:
                output[i] = 0
            else:
                output[i] = product// nums[i]
        return output
