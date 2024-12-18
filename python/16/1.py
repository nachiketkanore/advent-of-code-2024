from ordered_set import OrderedSet
mat = open('in').read().strip().split('\n')
# print(mat)
N, M = len(mat), len(mat[0])

def inside(i, j): return i in range(N) and j in range(M)
# print((N, M))

si, sj = 0, 0

for i in range(N):
    for j in range(M):
        if mat[i][j] == 'S':
            si, sj = i, j
            break
print(si, sj)
Q = OrderedSet([])
INF = int(1e5)
dp = [[INF for _ in range(M)] for _ in range(N)]
dp[si][sj] = 0

dirs1 = [ (0, 1), (-1, 0), (0, -1), (1, 0) ]
dirs2 = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
Q.add((0, si, sj, 0))

while len(Q) > 0:
    dist, x, y, dir = Q.pop(0)
    # Q.remove((dist, x, y, dir))

    if mat[x][y] == 'E':
        ex, ey = x, y
        print(f'ans = {dist}')
        print('here')
        # break

    idlx, idrx = (dir - 1 + 4) % 4, (dir + 1) % 4

    for j in (idlx, idrx):
        dx, dy = dirs1[j]
        nx, ny = x + dx, y + dy
        if inside(nx, ny) and mat[nx][ny] != '#' and (1000 + dist + 1) < dp[nx][ny]:
            dp[nx][ny] = 1000 + dist + 1
            Q.add((dp[nx][ny], nx, ny, j))

    dx, dy = dirs1[dir]
    nx, ny = x + dx, y + dy
    if inside(nx, ny) and mat[nx][ny] != '#' and (dist + 1) < dp[nx][ny]:
        dp[nx][ny] = dist + 1
        Q.add((dp[nx][ny], nx, ny, dir))
    
# for i in range(N):
#     print('  '.join(str(x) if x < INF else '....' for x in dp[i]))

print(f'ans = {dp[ex][ey]}')
