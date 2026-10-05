class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces_map = {'(': ')', '{': '}', '[': ']'}
        if len(s)%2 != 0:
            return False
        for c in s:
            if c in braces_map:
                stack.append(c)
            elif stack and c == braces_map[stack.pop()]:
                continue
            else:
                return False
        return True if not stack else False
