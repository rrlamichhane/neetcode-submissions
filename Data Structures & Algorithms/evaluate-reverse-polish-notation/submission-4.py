class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator_set = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t in operator_set:
                x = stack.pop()
                y = stack.pop()
                stack.append(int(eval(f"{y}{t}{x}")))
            else:
                stack.append(int(t))
        return stack[0]
