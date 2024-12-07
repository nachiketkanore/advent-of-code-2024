input = open('in').read().strip().split('\n')

A = [int(x.split('   ')[0]) for x in input]
B = [int(x.split('   ')[1]) for x in input]
A.sort(); B.sort()

print(sum(a * B.count(a) for a in A))
