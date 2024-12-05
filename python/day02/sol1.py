lines = open('in', 'r').read().strip().split('\n')

ans = 0
for line in lines:
    A = [int(x) for x in line.strip().split(' ')]

    B = sorted(A.copy())
    ok1 = A == B

    B = B[::-1]
    ok2 = A == B

    mn = min(abs(A[i] - A[i - 1]) for i in range(1, len(A)))
    mx = max(abs(A[i] - A[i - 1]) for i in range(1, len(A)))

    if (ok1 or ok2) and (mn > 0 and mx < 4): 
        ans += 1

print(ans)
