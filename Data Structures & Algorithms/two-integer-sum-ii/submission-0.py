class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                cur_sum = numbers[i] + numbers[j]
                if cur_sum == target:
                    return [i+1, j+1]
