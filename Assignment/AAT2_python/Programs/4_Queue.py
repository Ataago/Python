#4.	python program to implement Queue Operations.
queue = []
size = 10

def display_q():
    if len(queue) == 0:
        print("Empty")
    else:
        print("Queue is:", end=' ')
        for item in queue:
            print(item, end=' ')

def enQ(item):

    if len(queue) < size:
        queue.append(item)

    else:
        print("Queue is full")

def deQ():
    print("\ndeleted: ",queue[0])
    del queue[0]

display_q()
enQ(5)
enQ(1)
enQ(2)
enQ(4)
enQ(3)
display_q()
deQ()
display_q()
