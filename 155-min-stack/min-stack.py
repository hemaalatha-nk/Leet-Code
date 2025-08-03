class MinStack:

    def __init__(self):

        self.minStack=[]
        self.minValue=[]
        

    def push(self, val: int) -> None:
        self.minStack.append(val)
        
        if not self.minValue: 
            self.minValue.append(val)
        elif val> self.minValue[-1]:
            self.minValue.append(self.minValue[-1])
        else:
            self.minValue.append(val)
        

    def pop(self) -> None:
        self.minStack.pop()
        self.minValue.pop()
        
        

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        # print(self.minValue )
        return self.minValue[-1] 

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()