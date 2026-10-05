class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            new_target = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == new_target:
                    return [i+1, mid+1]
                elif numbers[mid] < new_target:
                    l = mid + 1
                else:
                    r = mid -1
        return []

    
    def twoSum_n2(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                cur_sum = numbers[i] + numbers[j]
                if cur_sum == target:
                    return [i+1, j+1]
