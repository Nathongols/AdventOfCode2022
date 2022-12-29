file = open(r"Day2\input.txt", "r")

score = 0

class Rank: 
    def __init__(self, char):
        self.char = char
        self.val = 0
        if (self.char == 'X' or self.char == 'A'):
            self.val = 1
        if (self.char == 'Y' or self.char == 'B'):
            self.val = 2       
        if (self.char == 'Z' or self.char == 'C'):
            self.val = 3

def compare(p1, p2):
    score = 0
    score += p2.val
    if (p1.val == 3 and p2.val == 1):
        score += 6
    elif (p1.val < p2.val and (p1.val != 1 or p2.val != 3)):
        score += 6
    elif (p1.val == p2.val):
        score += 3
    return score

for line in file: 
    message = line.split()
    score += compare(Rank(message[0]), Rank(message[1]))


print(score)