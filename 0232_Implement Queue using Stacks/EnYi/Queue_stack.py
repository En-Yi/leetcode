class MyQueue:

    def __init__(self):
        self.in_stack = []
        
    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:  
        self.out_stack = []      
        if not self.in_stack:
            return -1
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        a=self.out_stack.pop()
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
        return a

    def peek(self) -> int:
        return self.in_stack[0]

    def empty(self) -> bool:
        return len(self.in_stack) == 0