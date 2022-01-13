
with open('C:\\New folder\\demo.txt', 'r') as f:
    for line in iter(f.readline, ''):
        print(line.encode())
