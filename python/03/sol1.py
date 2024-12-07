import re
input = open("in", "r").read()

x = re.findall(r"mul\([0-9]+,[0-9]+\)", input)

ans1 = 0
for m in x:
    vals = m.split(',')
    a = vals[0][4:]
    b = vals[1][:-1]
    ans1 += int(a) * int(b)

print(ans1)
