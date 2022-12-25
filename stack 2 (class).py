class stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(item, " pushed to the stack ")
    def isempty(self):
        return len(self.stack)==0
    def pop(self):
        if self.isempty():
            return str(-maxsize-1)
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def display(self):
        print(" ".join (x for x in self.stack) )
        print(" ".join(self.stack [i] for i in range (len(self.stack))))
        print(" ".join(item for item in self.stack[::-1]))
#drive code

s=stack()
s.push(str(5))
s.push(str(10))
s.push(str(15))
s.push(str(20))
print(s.pop()," popped from the stack ")
print(str(s.size())," is the size of the stack ")
s.display()
