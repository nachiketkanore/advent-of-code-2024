lines = open('in', 'r').read().strip().split('\n')

ans = 0
for line in lines:
    A = [int(x) for x in line.strip().split(' ')]

    B = sorted(A.copy())
    ok1 = A == B

    B = B[::-1]
    ok2 = A == B
    ok3 = all(x>0 and x<4 for x in [abs(A[i-1]-A[i]) for i in range(1,len(A))])

    if (ok1 or ok2) and ok3:
        ans += 1

print(ans)
