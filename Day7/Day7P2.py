text = open(r"C:\Users\Nathg\Documents\Code\AdventOfCoding\Day7\input.txt", "r")

filepath = []
total = 0

class file:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class dirr:
    def __init__(self, name, size, parent, files, dirrs, flag):
        self.name = name
        self.size = size
        self.parent = parent
        self.files = files
        self.dirrs = dirrs
        self.flag = flag

    def addfile(self, file):
        if type(file) == dirr:
            self.dirrs.append(file)
        else:
            self.files.append(file)

    def getdirr(self, name):
        for x in self.dirrs:
            if x.name == name:
                return x

class system:
    def __init__(self, currentDir):
        self.currentDir = currentDir

    def cd(self, dir):
        self.currentDir = dir
        

    def ls(self):
        return self.currentDir.files

dir1 = dirr('/', 0, None, [], [], 0)
system = system(dir1)

for x in text:
    if x[0] == '$':
        input = x.split()
        if input[1] == 'cd':
            if input[2] == '..':
                system.currentDir.flag = 1
                system.cd(system.currentDir.parent)
            elif input[2] == '/':
                system.cd(dir1)
            else:
                system.currentDir.flag = 1
                system.cd(system.currentDir.getdirr(input[2]))
    elif system.currentDir.flag == 0:
        input = x.split()
        if input[0] == 'dir':
            system.currentDir.addfile(dirr(input[1], 0, system.currentDir, [], [], 0))
        else:
            system.currentDir.addfile(file(input[1], input[0]))
            system.currentDir.size += int(input[0])

def calculatesize(dir):
    for x in dir.dirrs:
        dir.size += calculatesize(x)
    filepath.append(dir.size)
    return dir.size

calculatesize(dir1)

requiredsize = 30000000-(70000000-dir1.size)
close = 1000000000
for x in filepath:
    if x < close and x >= requiredsize:
        close = x
print(close)