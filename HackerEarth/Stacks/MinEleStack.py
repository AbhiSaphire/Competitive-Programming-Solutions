class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        if len(self.s) == 0:
            self.minEle = x
            self.s.append(x)
        else:
            if self.minEle <= x:
                self.s.append(x)
            else:
                self.s.append((2 * x) - self.minEle)
                self.minEle = x

    def pop(self):
        if self.s:
            y = self.s.pop()
            if y >= self.minEle:
                return y
            if y < self.minEle:
                ret = self.minEle
                self.minEle = (2 * self.minEle) - y
                return ret
        else:
            return -1

    def getMin(self):
        if self.s:
            return self.minEle
        return -1   