#俩个栈实现队列
class StackToQueue():
    def __init__(self):
        self._stack1 = []
        self._stack2 = []
    def appendTail(self,x):
        self._stack1.append(x)
    def deleteHead(self):
        if self._stack2:
            return self._stack2.pop()
        else:
            if self._stack1:
                while self._stack1:
                    self._stack2.append(self._stack1.pop())
                return self._stack2.pop()
            else:
                return None
