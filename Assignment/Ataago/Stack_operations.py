#b.	Write a Python program to implement stackoperations  using  functions.

#list as stack
stack = []
size = 3

def Display_Stack():
    print("Stack :")
    for item in stack:
        print(item)

def Push(item):
    if len(stack) < size:
        stack.append(item)
    else:
        print("Stack is full!")

def Pop():
    if len(stack) > 0:
        stack.pop()         #pre defined function
    else:
        print("Stack is empty.")

#type what ever u want here
Push(1)
Push(2)
Push(3)
Display_Stack()
Push(4)
Display_Stack()
Pop()
Display_Stack()
