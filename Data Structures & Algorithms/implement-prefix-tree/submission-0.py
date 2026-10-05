class PrefixTree:
    end_marker = "END"

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        r = self.root
        for c in word:
            r[c] = r.get(c, {})
            r = r[c]
        r[self.end_marker] = True

    def search(self, word: str) -> bool:
        r = self.root
        for c in word:
            if c not in r:
                return False
            r = r[c]
        if self.end_marker not in r:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        r = self.root
        for c in prefix:
            if c not in r:
                return False
            r = r[c]
        return True
        
        