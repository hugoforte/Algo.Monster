from collections import deque 

#stacks FIFO
def heaps():
    my_stack = []
    my_stack.append('a string')
    my_stack.append(2)
    my_stack.append(False)

    while len(my_stack) > 0:
        print("Last item " + str(my_stack[-1]))
        my_stack.pop()

#queue LIFOs
def queues():
    queue = deque()
    queue.append('a string')
    queue.append(2)
    queue.append(False)

    print("First item " + str(queue[0]))
    queue.appendleft('I jumped the line')

    while len(queue) > 0:
        print('Next item ' + str(queue[0]))
        queue.popleft()


#arrays
def arrays():
    #simple array with two numbers
    my_arr = [6, 7]
    #print_arr(my_arr)

    my_arr = range(7)
    #print_arr(my_arr)
    
    #4 falses, slicing is left inclusive, so index 3,4,5 and 6
    #print_arr(my_arr[3:])

    #3 falses, slicing is right exclusive, so index 0,1, and 2
    #print_arr(my_arr[:3])

    #Prints nothing, as this says, print starting from index 3, but not including index 3
    print_arr(my_arr[3:3])


def print_arr(my_arr: []):
    for i, item in enumerate(my_arr):
        print ('the item at index: ' + str(i) + ' is ' + str(item))


#Hash set - for 'exists' questions
def sets():
    my_set = set()
    my_set.add(1)
    my_set.add('some string')
    my_set.add(False)
    my_set.add(True)
    print(True in my_set)
    my_set.remove(True)
    print(True in my_set)
    print('some string' in my_set)


#dictionaries
def dictionaries():
    my_dict = {2:2}
    my_dict[1] = 1
    print(1 in my_dict)
    print(2 in my_dict)
    print(my_dict[1])
    print(my_dict[2])


if __name__ == '__main__':
    #arrays()
    #stacks()
    #queues()
    #sets()
    dictionaries()