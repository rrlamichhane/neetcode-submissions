class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        max_len = 1
        len_seq = 1
        nums = sorted(nums)
        last_num = nums[0]
        print(nums, last_num)
        for n in nums[1:]:
            diff = n-last_num
            if diff == 0:
                continue
            elif diff == 1:
                len_seq += 1
                max_len = max(max_len, len_seq)
            else:
                len_seq = 1
            last_num = n
        return max_len
