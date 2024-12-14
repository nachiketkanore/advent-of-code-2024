import re
lines = open('in').read().strip().split('\n')

positions = []

for line in lines:
    y, x, dy, dx = map(int, re.findall(r'-*\d+', line))
    positions.append((x, y, dx, dy))

ITER = 100
N, M = 103, 101
for _ in range(ITER):
    npositions = []
    for x, y, dx, dy in positions:
        npositions.append(((x + dx + N) % N, (y + dy + M) % M, dx, dy))
    positions = npositions

check = [[0 for _ in range(M)] for _ in range(N)]

for x, y, dx, dy in positions:
    check[x][y] += 1

midN, midM = N // 2, M // 2

one, two, three, four = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if i < midN and j < midM:
            one += check[i][j]
        if i < midN and j > midM:
            two += check[i][j]
        if i > midN and j < midM:
            three += check[i][j]
        if i > midN and j > midM:
            four += check[i][j]

ans = one * two * three * four
print(f'ans = {ans}')
