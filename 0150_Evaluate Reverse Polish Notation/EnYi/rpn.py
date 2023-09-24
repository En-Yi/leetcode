class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def rpn(a, b, c):
            a = int(a)
            b = int(b)
            if c == "+":
                return a + b
            elif c == "-":
                return a - b
            elif c == "*":
                return int(a * b)
            elif c == "/":
                return int(a / b)
        items = ['+', '-', '*', '/']
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        for i in tokens:
            if i not in items:
                stack.append(i)
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(rpn(first, second, i))
        return stack[0]