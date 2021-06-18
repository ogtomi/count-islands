with open('example.txt', 'r') as f:
    content = f.read().split('\n')

M = len(content[0])
N = len(content) 

count = 0

for row in range(N):
    for col in range(M):
        if content[row][col] == 1:
            count += 1

print(count)
print("Lengths")
print(M)
print(N) 
