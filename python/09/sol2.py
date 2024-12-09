A = open('in', 'r').read().strip().split('\n')[0]

all = []
idx = 0

for i, ch in enumerate(A):
    if i % 2 == 1 and int(ch) > 0:
        all.append([('.', int(ch))])
    elif int(ch) > 0:
        all.append([(str(idx), int(ch))])
        idx += 1

for j in reversed(range(len(all))):
    # numeric groups from right to left: i ... j
    if len(all[j]) == 1 and all[j][0][0].isdigit():
        num, freq = all[j][0]
        for i in range(j):
            found = False
            for idx, (v, cnt) in enumerate(all[i]):
                if v == '.' and cnt >= freq:
                    all[i].pop(idx)
                    all[i].insert(idx, ('.', cnt - freq))
                    all[i].insert(idx, (num, freq))
                    all[j] = [('.', freq)]
                    found = True
                    break

            if found:
                break

seq = []
for x in all:
    for a, b in x:
        seq += [a for _ in range(int(b))]

ans = sum(i * int(ch) if ch != '.' else 0 for i, ch in enumerate(seq))
print(ans)




