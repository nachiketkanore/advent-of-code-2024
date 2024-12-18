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

# 11048(ans = 64) ex2 
# 7036(ans = 45) ex1
best = 82460 
TURNS = best // 1000
STRAIGHTS = best % 1000
cells = set()
visited = set()

def dfs(x, y, dir, turns, straight):
    global cells
    if mat[x][y] == '#' or turns > TURNS or straight > STRAIGHTS or (x, y) in visited:
        return
    if mat[x][y] == 'E':
        print('here', turns, straight)
        if turns == TURNS and straight == STRAIGHTS:
            cells.add((x, y))
            print(f'found ans = {len(cells)}')
            for a, b in visited:
                cells.add((a, b))
        return

    visited.add((x, y))
    # print(visited)
    # print(trace)

    idlx, idrx = (dir - 1 + 4) % 4, (dir + 1) % 4
    for j in (idlx, idrx):
        dx, dy = dirs[j]
        nx, ny = x + dx, y + dy
        # print(f'here for {x}, {y}, checking for {nx}, {ny}')
        if inside(nx, ny) and mat[nx][ny] != '#' and (nx, ny) not in visited:
            # print(f'going from ({x}, {y}) to ({nx}, {ny})')
            dfs(nx, ny, j, turns + 1, straight + 1)

    dx, dy = dirs[dir]
    nx, ny = x + dx, y + dy
    # print(f'here for {x}, {y}, diffs = {dx, dy} checking for {nx}, {ny}')
    if inside(nx, ny) and mat[nx][ny] != '#' and (nx, ny) not in visited:
        # print(f'going from ({x}, {y}) to ({nx}, {ny})')
        dfs(nx, ny, dir, turns, straight + 1)

    visited.remove((x, y))

dfs(si, sj, 0, 0, 0)

print(f'best = {best}')
print(f'ans = {len(cells)}')

