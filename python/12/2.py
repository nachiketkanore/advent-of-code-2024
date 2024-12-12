from collections import defaultdict
lines = open('in').read().strip().split('\n')
mat = [[ch for ch in line] for line in lines]
N, M = len(mat), len(mat[0])
dirs = [(0,1), (0,-1), (1,0), (-1,0)]

def inside(i, j): return i in range(N) and j in range(M)

vis = set()
curr = set()

def go(i, j, check):
    if not inside(i, j):
        return 
    if mat[i][j] != check:
        return 
    if (i, j) in vis:
        return
    vis.add((i, j))
    curr.add((i, j))
    for dx,dy in dirs:
        go(i + dx, j + dy, check)


comps = []

ans = 0
for i in range(N):
    for j in range(M):
        if not (i, j) in vis:
            curr.clear()
            go(i, j, mat[i][j])


            comp = []
            for x, y in curr:
                adj = 0
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not inside(nx, ny) or (inside(nx, ny) and mat[nx][ny] != mat[x][y]):
                        comp.append((x, y))
                        break
            comps.append((len(curr), comp))

ans = 0
for X, comp in comps:
    adj = defaultdict(list)
    for x, y in comp:
        # check sides belonging to a perimeter
        if not inside(x-1,y) or (inside(x-1, y) and mat[x-1][y] != mat[x][y]):
            adj[(x, y)].append((x, y + 1))
            adj[(x, y + 1)].append((x, y))
        if not inside(x+1,y) or (inside(x+1, y) and mat[x+1][y] != mat[x][y]):
            adj[(x + 1, y)].append((x + 1, y + 1))
            adj[(x + 1, y + 1)].append((x + 1, y))
        if not inside(x, y + 1) or (inside(x, y + 1) and mat[x][y + 1] != mat[x][y]):
            adj[(x, y + 1)].append((x + 1, y + 1))
            adj[(x + 1, y + 1)].append((x, y + 1))
        if not inside(x, y - 1) or (inside(x, y - 1) and mat[x][y - 1] != mat[x][y]):
            adj[(x, y)].append((x + 1, y))
            adj[(x + 1, y)].append((x, y))

    corners = 0

    for x, neigh in adj.items():
        ok = 0
        for check in [[(-1,0), (0,-1)], [(-1,0), (0,1)], [(0,1),(1,0)], [(0,-1), (1,0)]]:
            all = True
            for dx, dy in check:
                all &= neigh.count((x[0] + dx, x[1] + dy)) > 0
            if all:
                ok += 1
        corners += ok if ok & 1 else ok // 2

    score = X * corners
    ans += score
        
print(ans)
