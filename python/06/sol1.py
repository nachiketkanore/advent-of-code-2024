import sys
sys.setrecursionlimit(10**6)
mat = open('in').read().strip().split('\n')
N, M = len(mat), len(mat[0])

vis = set()

def inside(i, j): return i >= 0 and i < N and j >= 0 and j < M

def go(i, j, dir):
    if not inside(i, j) or mat[i][j] == '#':
        return 
    vis.add((i, j))

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
        if mat[ni][nj] == '#': # change direction
            if dir == 'u':
                go(i, j, 'r')
            elif dir == 'd':
                go(i, j, 'l')
            elif dir == 'l':
                go(i, j, 'u')
            elif dir == 'r':
                go(i, j, 'd')
        else: # move ahead
            go(ni, nj, dir)

si, sj = 0, 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == '^':
            si, sj = i, j
            break

go(si, sj, 'u')
ans = len(vis)
print(ans)

