input = open('in', 'r').read().split('\n\n')
A, Q = input[0], input[1]

before = [[False for _ in range(100)] for _ in range(100)]

for line in A.split('\n'):
    x = line.split('|')
    a, b = int(x[0]), int(x[1])
    before[a][b] = True

ans = 0
for line in Q.strip().split('\n'):
    A = [int(x) for x in line.split(',')]
    ok = True
    for i in range(len(A)):
        for j in range(len(A)):
            if i < j:
                ok &= before[A[i]][A[j]]
    if ok:
        ans += A[len(A) // 2]

assert(ans == 4662)
print(ans)

