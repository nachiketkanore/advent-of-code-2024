mat = [line for line in open('in', 'r').read().split('\n') if len(line) > 0];
N,M  = len(mat), len(mat[0])

def check(i, j, id, dx, dy):
    if id == len("XMAS"):
        return True
    if i < 0 or i >= N or j < 0 or j >= M:
        return False
    if mat[i][j] != "XMAS"[id]:
        return False
    return check(i + dx, j + dy, id + 1, dx, dy)


dirs = [ [0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

ans = 0
for i in range(N):
    for j in range(M):
        for dir in dirs:
            ans += check(i, j, 0, dir[0], dir[1])

print(ans)
