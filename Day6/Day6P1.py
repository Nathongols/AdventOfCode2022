
file = open(r"C:\Users\Nathg\Documents\Code\AdventOfCoding\Day6\input.txt", "r")

input = file.read()
marker = {}

for i, char in enumerate(input):
    marker[i] = char
    if len(marker) > 14:
        marker.pop(i-14)
    if len(set(marker.values())) == 14:
        break

print(set(marker.keys()))