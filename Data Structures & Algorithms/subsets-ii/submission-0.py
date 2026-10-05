class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        self.backtrack_subsets(0, nums, [])
        return self.ans

    def backtrack_subsets(self, i, nums: List[int], css: List[int]):
        self.ans.append(css[::])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]:
                continue
            css.append(nums[j])
            self.backtrack_subsets(j+1, nums, css)
            css.pop()
