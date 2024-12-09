A = open('in', 'r').read().strip().split('\n')[0]

all = []
idx = 0
for i, ch in enumerate(A):
    if i & 1:
        all += ['.' for _ in range(int(ch))]
    else:
        all += [str(idx) for _ in range(int(ch))]
        idx += 1

def check(A):
    last_digit = -1
    first_dot = -1
    for i, ch in enumerate(A):
        if ch == '.':
            if first_dot == -1: first_dot = i
        else:
            last_digit = i
    return last_digit < first_dot

def first_dot(A):
    for i, ch in enumerate(A):
        if ch == '.':
            return i
    return int(1e9)

def last_digit(A):
    ans = int(1e9)
    for i, ch in enumerate(A):
        if ch != '.':
            ans = i
    return ans

while not check(all):
    dot, dig = first_dot(all), last_digit(all)
    all[dot], all[dig] = all[dig], all[dot]

ans = sum(i * int(all[i]) for i in range(last_digit(all) + 1))
print(ans)
