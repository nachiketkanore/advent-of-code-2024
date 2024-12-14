import re
lines = open('in').read().strip().split('\n')

positions = []

for line in lines:
    y, x, dy, dx = map(int, re.findall(r'-*\d+', line))
    positions.append((x, y, dx, dy))

def display(positions):
    check = [[0 for _ in range(M)] for _ in range(N)]
    for x, y, _, _ in positions:
        check[x][y] += 1
    for i in range(N):
        print(''.join(str('.' if not cnt else cnt) for cnt in check[i]))

N, M = 103, 101
time = 0
while True:
    npositions = []
    for x, y, dx, dy in positions:
        npositions.append(((x + dx + N) % N, (y + dy + M) % M, dx, dy))
    time += 1
    positions = npositions
    unique = set((x, y) for x, y, _, _ in positions)
    if len(unique) == len(positions):
        display(positions)
        print(f'ans = {time}')
        break
