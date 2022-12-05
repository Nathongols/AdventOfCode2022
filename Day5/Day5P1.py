
file = open(r"C:\Users\Nathg\Documents\Code\AdventOfCoding\Day5\input.txt", "r")


tower = [[],[],[],[],[],[],[],[],[]]

def execute_move(_amount, _from, _to):
    for x in range(0,_amount):
        tower[_to-1].insert(0, get_top_block(_from-1))
        tower[_from-1].remove(get_top_block(_from-1))

def get_top_block(index):
    for x in tower[index]:
        if x != None and x.isalpha():
            return x

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
