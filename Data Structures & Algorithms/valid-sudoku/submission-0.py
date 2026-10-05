from collections import defaultdict

class Solution:
    def is_valid_char(self, c):
        if c.isnumeric():
            c_int = int(c)
            if c_int >=0 and c_int <= 9:
                return True
        elif c == ".":
            return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        grid_map = defaultdict(set)
        
        idx = 0
        for i, row in enumerate(board):
            for j, y in enumerate(row):
                item = row[j]
                if not self.is_valid_char(item):
                    return False
                if item == ".":
                    continue
                square = (i//3, j//3)
                if item in col_map[j] or item in row_map[i] or item in grid_map[square]:
                    return False
                
                col_map[j].add(item)
                row_map[i].add(item)
                grid_map[square].add(item)
        return True
