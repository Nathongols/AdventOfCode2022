
file = open(r"C:\Users\Nathg\Documents\School\AdventOfCoding\Day4\input.txt", "r")

total = 0

for x in file:
    pair = x.split(',')
    first = range(int(pair[0].split("-")[0]), int(pair[0].split("-")[1])+1)
    second = range(int(pair[1].split("-")[0]), int(pair[1].split("-")[1])+1)
    if set(first).issubset(second) or set(second).issubset(first) or set(first) == set(second):
        total += 1
        
print(total)