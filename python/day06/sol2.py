import sys
from tqdm import tqdm
sys.setrecursionlimit(10**7)

mat = open('ex').read().strip().split('\n')
mat = [[ch for ch in row] for row in mat]
N, M = len(mat), len(mat[0])
print(N, M)

def inside(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

check = set()

def go(i, j, dir):
    if not inside(i, j):
        return False
    if mat[i][j] == '#':
        return False
    if (i, j, dir) in check:
        return True

    check.add((i, j, dir))

    dx, dy = 0, 0
    if dir == 'u':
        dx, dy = -1,0
    elif dir == 'd':
        dx, dy = +1, 0
    elif dir == 'l':
        dx, dy = 0, -1
    elif dir == 'r':
        dx, dy = 0, +1

    ni, nj = i + dx, j + dy

    if inside(ni, nj):
        if mat[ni][nj] == '#':
            if dir == 'u':
                return go(i, j, 'r')
            elif dir == 'd':
                return go(i, j, 'l')
            elif dir == 'l':
                return go(i, j, 'u')
            elif dir == 'r':
                return go(i, j, 'd')
        else:
            return go(ni, nj, dir)

    return False






si, sj = 0, 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == '^':
            si, sj = i, j
            break


progress = 0
ans = 0
for i in tqdm(range(N)):
    for j in range(M):
        progress += 1
        if mat[i][j] == '.':

            mat[i][j] = '#'
            check.clear()

            if go(si, sj, 'u'):
                ans += 1

            mat[i][j] = '.'

        if progress % 1000 == 0:
            print(progress)
# go(si, sj, 'u')
print(ans)

