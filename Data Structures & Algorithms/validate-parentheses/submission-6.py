class Solution:
    def isValid(self, s: str) -> bool:
        braces_map = { '(': ')', '{': '}', '[': ']' }
        braces_stack = []
        for c in s:
            if c in braces_map:
                braces_stack.append(braces_map[c])
                continue
            if not braces_stack:
                return False
            closing_brace = braces_stack.pop()
            if c != closing_brace:
                return False
        return len(braces_stack) == 0
        