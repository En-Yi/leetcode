class MinStack:
    def __init__(self):
        self.stack = []  # 存主要 stack
        self.min_stack = []  # 存最小值 stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:  
            # 如果最小值stack沒元素或val小於最小值
            self.min_stack.append(val)  # 加入最小值stack，因此為遞減數列

    def pop(self) -> None:
        if self.stack:  
            if self.stack[-1] == self.min_stack[-1]:  # 如果stack跟最小值stack的最後一個元素相同
                self.min_stack = self.min_stack[0:len(self.min_stack)-1] # 丟出最小值stack最後一個元素
            self.stack = self.stack[0:len(self.stack)-1]

    def top(self) -> int:
        if self.stack:  
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:  
            return self.min_stack[-1] # 返回最後一個元素，也是最小值