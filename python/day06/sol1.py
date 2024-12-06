import sys
sys.setrecursionlimit(10**6)
mat = open('in').read().strip().split('\n')
print(mat)
N, M = len(mat), len(mat[0])

vis = [[False for _ in range(500)] for _ in range(500)]

def inside(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

def go(i, j, dir):
    if not inside(i, j):
        return 
    if mat[i][j] == '#':
        return
    # if vis[i][j]:
    #     return 
    vis[i][j] = True

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
                go(i, j + 1, 'r')
            elif dir == 'd':
                go(i, j - 1, 'l')
            elif dir == 'l':
                go(i - 1, j, 'u')
            elif dir == 'r':
                go(i + 1, j, 'd')
        else:
            go(ni, nj, dir)






si, sj = 0, 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == '^':
            si, sj = i, j
            break


go(si, sj, 'u')

ans = 0
for i in range(N):
    for j in range(M):
        ans += vis[i][j]
print(ans)

