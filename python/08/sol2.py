mat = [line for line in open('in', 'r').read().split('\n') if len(line) > 0];
N,M  = len(mat), len(mat[0])

pos = {}

for i in range(N):
    for j in range(M):
        if mat[i][j] in pos:
            pos[mat[i][j]].append((i, j))
        else:
            pos[mat[i][j]] = [(i, j)]

pos.pop('.')

def dist(a,  b): return abs(a[0] - b[0]) + abs(a[1] - b[1])
def inside(i, j): return i in range(N) and j in range(M)

check = set()

for k, v in pos.items():
    for x1, y1 in v:
        for x2, y2 in v:
            # first diagonal direction
            if x1 < x2 and y1 < y2:
                dx, dy = abs(x2 - x1), abs(y2 - y1)
                x, y = x1, y1

                while inside(x, y):
                    check.add((x, y))
                    x, y = x - dx, y - dy
                x, y = x2, y2
                while inside(x, y):
                    check.add((x, y))
                    x, y = x + dx, y + dy

            # first diagonal direction
            if x1 > x2 and y1 < y2:
                dx, dy = abs(x2 - x1), abs(y2 - y1)
                x, y = x1, y1

                while inside(x, y):
                    check.add((x, y))
                    x, y = x + dx, y - dy
                x, y = x2, y2
                while inside(x, y):
                    check.add((x, y))
                    x, y = x - dx, y + dy
print(len(check))
