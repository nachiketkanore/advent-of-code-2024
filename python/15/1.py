lines = open('in').read().strip().split('\n\n')

mat = [[ch for ch in line] for line in lines[0].split('\n')]
N, M = len(mat), len(mat[0])

moves = { '<': (0,-1), '>': (0,1), '^': (-1,0), 'v': (1,0) }

def inside(i, j): return i in range(N) and j in range(M)

cx, cy = -1,-1
for i in range(N):
    for j in range(M):
        if mat[i][j] == '@':
            cx, cy = i, j; break;

Q = ''.join(lines[1].split('\n'))
print(Q)
for q in Q:
    dx, dy = moves[q]
    nx, ny = cx + dx, cy + dy
    if mat[nx][ny] == '.':
        mat[cx][cy] = '.'
        mat[nx][ny] = '@'
        cx, cy = nx, ny
    elif mat[nx][ny] == 'O':
        x, y = nx, ny
        while inside(x, y) and mat[x][y] != '.':
            if mat[x][y] == '#': break
            x, y = x + dx, y + dy
        if inside(x, y) and mat[x][y] == '.':
            mat[nx][ny] = '@'
            mat[cx][cy] = '.'
            mat[x][y] = 'O'
            cx, cy = nx, ny
    
    # print(f'check = {q}')
    # for row in mat:
    #     print(''.join(row))

for row in mat:
    print(''.join(row))


ans = 0
for i in range(N):
    for j in range(M):
        if mat[i][j] == 'O':
            ans += 100 * i + j
print(ans)


