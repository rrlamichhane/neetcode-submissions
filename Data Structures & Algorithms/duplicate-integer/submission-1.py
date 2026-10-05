class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for x in nums:
            if x in num_set:
                return True
            num_set.add(x)
        
        return False
        