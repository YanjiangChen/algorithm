#俩个队列实现栈
class QueueToStack():
    def __init__(self):
        self._stack1 = []
        self._stack2 = []
    def push(self,x):
        if len(self._stack1) == 0:
            self._stack1.append(x)
        elif len(self._stack2) == 0:
            self._stack2.append(x)
        if len(self._stack2) == 1 and len(self._stack1) >= 1:
            while self._stack1:
                self._stack2.append(self._stack1.pop(0))
        elif len(self._stack1) == 1 and len(self._stack2) >= 1:
            while self._stack2:
                self._stack1.append(self._stack2.pop(0))
    def pop(self):
        if self._stack1:
            return self._stack1.pop(0)
        elif self._stack2:
            return self._stack2.pop(0)
        else:
            return None
