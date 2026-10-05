class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def find_subbox(r, c):
            rbox = r//3
            cbox = c//3
            print(r, c, rbox, cbox)
            return f"{rbox}_{cbox}"

        items_map = {}
        for r in range(len(board)):
            for c in range(len(board[0])):
                cur_item = board[r][c]
                if cur_item == ".":
                    continue
                subbox = find_subbox(r, c)
                cur_sections = [f"row_{r}", f"col_{c}", subbox]
                print(cur_sections)
                for sect in cur_sections:
                    if sect not in items_map:
                        items_map[sect] = {cur_item}
                    elif cur_item in items_map[sect]:
                        print(cur_item, r, c, subbox)
                        return False
                    else:
                        items_map[sect].add(cur_item)

        return True
        