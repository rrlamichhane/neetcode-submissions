class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "-", "*", "/"}
        integers = []

        for t in tokens:
            if t in operands:
                op2, op1 = integers.pop(), integers.pop()
                result = eval(str(op1) + t + str(op2))
                integers.append(int(result))
            else:
                integers.append(int(t))
        
        return integers[-1]
