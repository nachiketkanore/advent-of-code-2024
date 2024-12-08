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
    for i in range(len(v)):
        for j in range(len(v)):
            if i != j:
                x1, y1 = v[i]
                x2, y2 = v[j]

                if x1 < x2 and y1 < y2:
                    dx, dy = abs(x2 - x1), abs(y2 - y1)
                    x, y = x1 - dx, y1 - dy
                    check.add((x, y))
                    x, y = x2 + dx, y2 + dy
                    check.add((x, y))
                if x1 > x2 and y1 < y2:
                    dx, dy = abs(x2 - x1), abs(y2 - y1)
                    x, y = x1 + dx, y1 - dy
                    check.add((x, y))
                    x, y = x2 - dx, y2 + dy
                    check.add((x, y))

print(sum(inside(x, y) for x, y in check))
