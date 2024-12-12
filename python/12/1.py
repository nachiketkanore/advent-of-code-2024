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



ans = 0
for i in range(N):
    for j in range(M):
        if not (i, j) in vis:
            curr.clear()
            go(i, j, mat[i][j])
            area = len(curr)
            peri = 0
            for x, y in curr:
                adj = 0
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not inside(nx, ny) or (inside(nx, ny) and mat[nx][ny] != mat[x][y]):
                        adj += 1
                peri += adj
            ans += area * peri

print(ans)
