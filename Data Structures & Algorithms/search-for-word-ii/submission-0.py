class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, w):
        r = self
        for c in w:
            r.children[c] = r.children.get(c, TrieNode())
            r = r.children[c]
        r.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_root = TrieNode()

        for w in words:
            trie_root.add_word(w)

        rows, cols = len(board), len(board[0])
        output, visited = set(), set()
        
        def dfs(r, c, node, cur_word):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in node.children or (r,c) in visited:
                return
            visited.add((r,c))
            char = board[r][c]
            node = node.children[char]
            cur_word += char
            if node.is_word:
                output.add(cur_word)

            dfs(r+1, c, node, cur_word)
            dfs(r-1, c, node, cur_word)
            dfs(r, c+1, node, cur_word)
            dfs(r, c-1, node, cur_word)
            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie_root, "")
        
        return list(output)
