lines = [line for line in open('in', 'r').read().split('\n') if len(line) > 0]
mat = [[int(ch) if ch != '.' else '.' for ch in line] for line in lines]
N,M  = len(mat), len(mat[0])

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def inside(i, j): return i in range(N) and j in range(M)

def go(i, j, val, trace):
    if val == 9: return 1
    ans = 0
    for dx, dy in dirs:
        ni, nj = i + dx, j + dy
        if inside(ni, nj) and (val + 1 == mat[ni][nj]):
            ans += go(ni, nj, val + 1, trace + [(ni, nj)])
    return ans

ans = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            ans += go(i, j, 0, [(i, j)])

print(ans)
