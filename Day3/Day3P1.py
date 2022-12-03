
file = open(r"C:\Users\Nathg\Documents\School\AdventOfCoding\Day3\input.txt", "r")

Items = []
total = 0
for x in file: 
    firstpart, secondpart = x[:len(x)//2], x[len(x)//2:]
    Items += list(set(firstpart)&set(secondpart))
                

for x in Items:
    if x.isupper():
        total += ord(x)-38
    elif x.islower():
        total += ord(x)-96

print(total)