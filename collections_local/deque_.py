from collections import deque

"""
    deque: it allow to manage with a best way the lists improving the execution time
    deuqes are more slow than lists when we want to access to a middle items of a deque
    arguments: 
        1. maxlen= max items in a deque object
    
    Methods:
        1. popleft(): removes the left item
        2. pop() : remove the right element, it does not alow to remove an specific element
        2. clear(): clean all the elements
        3. extendsleft(): extends the deque
        4. insert(i, value): insert a value in a specific index o a deque
        5. a_deque[i]: recover an element
        6. del a_deque[i]: delete an element in a specific index
        7. count(value): count a value
        8. reverse()
        9. clear()
        
        References:  https://realpython.com/python-deque/
"""

q = deque()

numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
d = deque(numbers.items())

for i in range(3):
    q.append(i)
q.appendleft(3)

q.extend([5, 6, 7, 'test'])
q.rotate(2)  # This will rotate the last items to the first places
print(q)
