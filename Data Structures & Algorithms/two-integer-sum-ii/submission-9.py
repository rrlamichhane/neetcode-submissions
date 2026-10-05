class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        while l < len(numbers)-1:
            cur_target = target - numbers[l]
            r = l + 1
            print(l, r, len(numbers))
            while r < len(numbers) and cur_target >= numbers[r]:
                if cur_target == numbers[r]:
                    return [l+1, r+1]
                r += 1
            l += 1
        return False
        