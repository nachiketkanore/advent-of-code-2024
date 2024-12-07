lines = open('in').read().strip().split('\n')

def go(id, vals, curr, T):
    if id == len(vals):
        return curr == T
    ans = False
    ans |= go(id + 1, vals, curr + vals[id], T)
    ans |= go(id + 1, vals, curr * vals[id], T)
    ncurr = int(str(curr) + str(vals[id]))
    ans |= go(id + 1, vals, ncurr, T)

    return ans

ans = 0
for line in lines:
    s = line.split(':')
    T = int(s[0])
    vals = list(map(int, s[1].strip().split(' ')))
    ans += T if go(1, vals, vals[0], T) else 0

print(ans)
