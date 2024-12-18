import heapq
import sys
sys.setrecursionlimit(10**9)

mat = open('in').read().strip().split('\n')
# print(mat)
N, M = len(mat), len(mat[0])

def inside(i, j): return i in range(N) and j in range(M)
print((N, M))

si, sj = 0, 0
ex, ey = 0, 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 'S':
            si, sj = i, j
        if mat[i][j] == 'E':
            ex, ey = i, j

print((si, sj), (ex, ey))

INF = int(1e9)

dirs = [ (0, 1), (-1, 0), (0, -1), (1, 0) ]

best = 82460
cells = set()
visited = set()
def dfs(x, y, dir, cost, trace=[]):
    global cnt, best, cells
    if mat[x][y] == '#' or cost > best or (x, y) in visited:
        return
    if mat[x][y] == 'E':
        print(f'checking ans = {len(cells)}')
        if cost == best:
            for a, b in trace:
                cells.add((a, b))
        return

    visited.add((x, y))
    # print(trace)

    idlx, idrx = (dir - 1 + 4) % 4, (dir + 1) % 4
    for j in (idlx, idrx):
        dx, dy = dirs[j]
        nx, ny = x + dx, y + dy
        # print(f'here for {x}, {y}, checking for {nx}, {ny}')
        if inside(nx, ny) and mat[nx][ny] != '#' and (nx, ny) not in visited:
            # print(f'going from ({x}, {y}) to ({nx}, {ny})')
            dfs(nx, ny, j, 1000 + cost + 1, trace + [(nx, ny)])

    dx, dy = dirs[dir]
    nx, ny = x + dx, y + dy
    # print(f'here for {x}, {y}, diffs = {dx, dy} checking for {nx}, {ny}')
    if inside(nx, ny) and mat[nx][ny] != '#' and (nx, ny) not in visited:
        # print(f'going from ({x}, {y}) to ({nx}, {ny})')
        dfs(nx, ny, dir, cost + 1, trace + [(nx, ny)])

    visited.remove((x, y))

dfs(si, sj, 0, 0, [(si, sj)])

print(f'best = {best}')
print(f'ans = {len(cells)}')

