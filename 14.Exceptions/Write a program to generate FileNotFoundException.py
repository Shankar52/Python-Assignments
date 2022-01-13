'''import sys

try:
    file1 = open("d:/mytext2.txt", "r")

except FileNotFoundError:
        print("Sorry file not found")
        sys.exit()

s = file1.read()

print(s)

file1.close()'''


import sys
file = open('myfile.txt')
lines = file.readline()
slines = int(lines.strip())
