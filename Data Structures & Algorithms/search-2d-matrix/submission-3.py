class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            rm = ( l + r) // 2
            if matrix[rm][0] > target:
                r = rm - 1
            elif matrix[rm][-1] < target:
                l = rm + 1
            else:
                break
        
        l, r = 0, len(matrix[rm])-1
        while l <= r:
            cm = (l + r) // 2
            if matrix[rm][cm] < target:
                l = cm + 1
            elif matrix[rm][cm] > target:
                r = cm - 1
            else:
                return True
        
        return False
