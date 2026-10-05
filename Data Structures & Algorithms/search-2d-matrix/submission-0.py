class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = l + ((r - l)// 2)
            cur_row = matrix[m]
            if cur_row[0] <= target <= cur_row[-1]:
                break
            elif cur_row[-1] < target:
                l = m + 1
            else:
                r = m - 1
        l, r = 0, len(cur_row) - 1
        while l <= r:
            m = l + ((r - l)// 2)
            if cur_row[m] < target:
                l = m + 1
            elif cur_row[m] > target:
                r = m - 1
            else:
                return True
        return False
        