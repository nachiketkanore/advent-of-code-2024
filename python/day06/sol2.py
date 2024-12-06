import sys
sys.setrecursionlimit(10**7)

mat = open('ex').read().strip().split('\n')
mat = [[ch for ch in row] for row in mat]
N, M = len(mat), len(mat[0])
# print(N, M)
# print(mat)

vis = [[0 for _ in range(N)] for _ in range(M)]

def inside(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

check = set()

def go(i, j, dir):
    if not inside(i, j):
        return False
    if mat[i][j] == '#':
        return False
    if vis[i][j] >= 10:
        return True
        # if (i, j, dir) in check:
        #     return True

    vis[i][j] += 1
    # if vis[i][j] > 1:
    #     check.add((i, j, dir))

    dx, dy = 0, 0
    if dir == 'u':
        dx, dy = -1,0
    elif dir == 'd':
        dx, dy = +1, 0
    elif dir == 'l':
        dx, dy = 0, -1
    elif dir == 'r':
        dx, dy = 0, +1
    else:
        assert(False)

    ni, nj = i + dx, j + dy

    if inside(ni, nj):
        if mat[ni][nj] == '#':
            if dir == 'u':
                return go(i, j + 1, 'r')
            elif dir == 'd':
                return go(i, j - 1, 'l')
            elif dir == 'l':
                return go(i - 1, j, 'u')
            elif dir == 'r':
                return go(i + 1, j, 'd')
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
for i in range(N):
    for j in range(M):
        progress += 1
        if mat[i][j] == '.':

            for x in range(N): 
                for y in range(M): 
                    vis[x][y] = 0

            mat[i][j] = '#'
            check.clear()

            if go(si, sj, 'u'):
                ans += 1
                mat[i][j] = 'X'
                # for x in range(N): 
                #     print([''.join(v) for v in mat[x]])
                # print()
                # for x in range(N): 
                #     print([v for v in vis[x]])

            mat[i][j] = '.'

        if progress % 1000 == 0:
            print(progress)
# go(si, sj, 'u')
print(ans)

