class Solution:
    def isValid(self, s: str) -> bool:
        braces_map = { '(': ')', '{': '}', '[': ']' }
        braces_stack = []
        for c in s:
            if c in braces_map:
                braces_stack.append(braces_map[c])
                continue
            if braces_stack and braces_stack[-1] == c:
                braces_stack.pop()
            else:
                return False
        return len(braces_stack) == 0
        