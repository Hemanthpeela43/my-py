#we are using -1 value when our stack is empty
from sys import maxsize
def push(stack,item):
    stack.append(item)
    print(item," pushed to stack ")
def isEmpty(stack):
    return len(stack)==0

def peak(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack[len(stack)-1]

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack.pop()
def creatstack ():
    stack=[]
    return stack
#drive code
stack= creatstack()
push(stack,str(5))
push(stack,str(10))
push(stack,str(15))
push(stack,str(20))
print(pop(stack) + " poped from stack ")
print(peak(stack))
print(peak(stack))
