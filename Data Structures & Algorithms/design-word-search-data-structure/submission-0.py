class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        r = self.root
        for c in word:
            r.children[c] = r.children.get(c, TrieNode())
            r = r.children[c]
        r.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            r = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in r.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in r.children:
                        return False
                    r = r.children[c]
            return r.word
        
        return dfs(0, self.root)
