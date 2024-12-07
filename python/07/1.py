lines = open('in').read().strip().split('\n')

ans = 0
for line in lines:
    s = line.split(':')
    T = int(s[0])
    vals = list(map(int, s[1].strip().split(' ')))
    req = len(vals) - 1
    for mask in range(1<<req):
        check = vals[0]
        for i in range(req):
            if mask >> i & 1:
                check += vals[i + 1]
            else:
                check *= vals[i + 1]

        if check == T:
            ans += T
            break
print(ans)
