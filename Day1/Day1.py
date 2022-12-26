import fibonacciHeap

file = open(r"Day1\input.txt", "r")

temp = 0
max = fibonacciHeap.FibonacciHeap()

for x in file:
    if (x == "\n"):
        max.insert_node(temp)
        temp = 0
    else:
        temp += int(x)


print (max.extract_max() + max.extract_max() + max.extract_max())