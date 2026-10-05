class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        ans = float("+inf")

        def jump_recur(count, idx):
            distance = nums[idx]
            if idx + distance + 1 >= len(nums):
                nonlocal ans
                ans = min(ans, count+1)
                return
            for i in range(1, distance+1):
                jump_recur(count+1, idx+i)

        jump_recur(0, 0)
        return ans
