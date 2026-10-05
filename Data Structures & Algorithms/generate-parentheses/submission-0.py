class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_pairs = set()

        def check_parenthesis_pair(s: str) -> bool:
            if len(s)%2 != 0:
                return False
            stack = []
            for c in s:
                if c == "(":
                    stack.append(c)
                elif c == ")":
                    if stack and stack.pop() == "(":
                        continue
                    else:
                        return False
                else:
                    return False
            return not stack

        def find_parenthesis_pairs(all_pairs, cur_pair, n):
            if len(cur_pair) == n:
                if check_parenthesis_pair(cur_pair):
                    all_pairs.add(cur_pair)
            if len(cur_pair) == n:
                return None
            find_parenthesis_pairs(all_pairs, cur_pair + "(", n)
            find_parenthesis_pairs(all_pairs, cur_pair + ")", n)

        find_parenthesis_pairs(all_pairs, "(", n*2)
        return list(all_pairs)
        