from typing import List, Dict, Set, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.word: Optional[str] = None  # Store complete word at terminal node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Uses Trie to store all words and backtracking DFS from each cell to find matches.
        Words found are collected in a result set for uniqueness.
        Trie enables pruning search paths early if no further word is possible from prefix.
        """
        def build_trie(words: List[str]) -> TrieNode:
            root = TrieNode()
            for word in words:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.word = word  # Mark the end of a word
            return root

        def dfs(row: int, col: int, parent: TrieNode):
            letter = board[row][col]
            curr_node = parent.children[letter]
            if curr_node.word:
                result.add(curr_node.word)
                curr_node.word = None  # De-duplicate; avoid multiple matches of same word
            # Mark the cell as visited
            board[row][col] = '#'
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_row, new_col = row + dr, col + dc
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    board[new_row][new_col] in curr_node.children):
                    dfs(new_row, new_col, curr_node)
            # Restore the cell
            board[row][col] = letter
            # Optional: prune leaf node
            if not curr_node.children:
                parent.children.pop(letter)

        root = build_trie(words)
        rows, cols = len(board), len(board[0])
        result: Set[str] = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return list(result)