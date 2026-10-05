class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if cur_sum < target:
                l += 1
            elif cur_sum > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []

    def twoSum_hashmap_n(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i, n in enumerate(numbers):
            if n in mp:
                return [mp[n]+1, i+1]
            mp[target-n] = i
        return []

    def twoSum_nlogn(self, numbers: List[int], target: int) -> List[int]:
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
