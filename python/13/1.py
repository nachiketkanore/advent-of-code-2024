import re
lines = open('in').read().strip().split('\n\n')

INF = int(1e20)
ans = 0
for line in lines:
    nums = re.findall(r'\d+', line)
    ax, ay, bx, by, X, Y = map(int, nums)

    B = (X * ay - Y * ax) // (bx * ay - ax * by)
    best = INF
    A1 = (X - B * bx) // ax
    A2 = (Y - B * by) // ay
    for A in (A1, A2):
        if (A * ax + B * bx) == X and (A * ay + B * by) == Y:
            best = min(best, 3 * A + B)
    if best < INF:
        ans += best
print(ans)
