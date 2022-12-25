# stack method 3 easyto create if stack is full then we have to add it to the another list
#hence we use this method to append the fulled list to another list

from collections import deque
stack=deque[]
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
top=stack[-1]
print(top)
size=len(stack)
print(size)
print(stack.pop())
