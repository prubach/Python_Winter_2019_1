import os



dir = 'h:\\'
files = os.listdir(dir)

for file in files:
    #print(file)
    if os.path.isdir(os.path.join(dir, file)):
        print(file)

print()
print(os.getcwd())

in_file = '..\\test\\run.m'
#in_file = 't.txt'
print(os.path.getsize(in_file))


with open(in_file, 'r') as in_f:
    for line in in_f.readlines():
        print(line)