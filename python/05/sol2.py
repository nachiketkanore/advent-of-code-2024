input = open('in', 'r').read().split('\n\n')
A, Q = input[0], input[1]

before = [[False for _ in range(100)] for _ in range(100)]

for line in A.split('\n'):
    vals = line.split('|')
    a, b = int(vals[0]), int(vals[1])
    before[a][b] = True

def check(vals):
    ok = True
    for i in range(len(vals)):
        for j in range(len(vals)):
            if i < j:
                ok &= before[vals[i]][vals[j]]
    return ok

ans = 0
for line in Q.strip().split('\n'):
    vals = [int(x) for x in line.split(',')]

    if not check(vals):
        for i in range(len(vals)):
            for j in range(len(vals)):
                if i < j and not before[vals[i]][vals[j]]:
                    vals[i], vals[j] = vals[j], vals[i]
        ans += vals[len(vals) // 2]

assert(ans == 5900)
print(ans)

