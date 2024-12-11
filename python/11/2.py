from collections import defaultdict
lines = open('in').read().strip().split('\n')
A = list(map(int, lines[0].split()))

counter = defaultdict(int)

for a in A:
    counter[a] += 1

for _ in range(75):
    counter_new = defaultdict(int)

    for v, freq in counter.items():

        if v == 0:
            counter_new[1] += freq

        elif len(str(v)) % 2 == 0:
            N = len(str(v))

            counter_new[int(str(v)[:N//2])] += freq
            counter_new[int(str(v)[N//2:])] += freq

        else:
            counter_new[2024*v] += freq

    counter = counter_new

ans = sum(cnt for _, cnt in counter.items())
print(ans)
