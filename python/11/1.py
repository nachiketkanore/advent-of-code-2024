lines = open('in').read().strip().split('\n')
A = list(map(int, lines[0].split()))

for _ in range(25):
    A_new = []
    for a in A:
        if a == 0:
            A_new.append(1)
        elif len(str(a)) % 2 == 0:
            N = len(str(a))
            A_new.append(int(str(a)[:N//2]))
            A_new.append(int(str(a)[N//2:]))
        else:
            A_new.append(2024 * a)
    A = A_new

print(len(A))
