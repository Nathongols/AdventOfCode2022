
file = open(r"C:\Users\Nathg\Documents\School\AdventOfCoding\Day3\input.txt", "r")

filelist = []
Items = []
total = 0

for x in file:
    filelist.append(x)

for i in range(0,len(filelist),3):
    Items += list(set(filelist[i])&set(filelist[i+1])&set(filelist[i+2]))

for x in Items:
    if x.isupper():
        total += ord(x)-38
    elif x.islower():
        total += ord(x)-96

print(total)