
file = open(r"C:\Users\Nathg\Documents\Code\AdventOfCoding\Day5\input.txt", "r")


tower = [[],[],[],[],[],[],[],[],[]]

def execute_move(_amount, _from, _to):
    for x in reversed(get_top_blocks(_from-1, _amount)):
        tower[_to-1].insert(0, x)
        tower[_from-1].remove(x)

def get_top_blocks(index, amount):
    package = []
    for x in tower[index]:
        if x != None and x.isalpha():
            package.append(x)
        if len(package) == amount:
            print (package)
            return package

for x, line in enumerate(file):
    if x < 8:
        temp = []
        for y in range(1,37,4):
            temp.append(line[y]);
        for z in range(0,9):
            if temp[z] != " ":
                tower[z].append(temp[z])
    if x > 9:
        execute_move(int(line.split()[1]), int(line.split()[3]), int(line.split()[5]))
    if x > 512:
        break

for x in tower:
    print(x[0])
