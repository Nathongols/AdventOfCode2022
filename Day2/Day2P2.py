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
    if (p2.char == 'X'):
        score += p1.val-1
        if(p1.char == 'A'):
            score += 3
    elif (p2.char == 'Y'):
        score += p1.val+3
    else:
        score += 6
        if(p1.char == 'C'):
            score += 1
        else:
            score += p1.val+1
    
    return score

for line in file: 
    message = line.split()
    score += compare(Rank(message[0]), Rank(message[1]))

print(score)