import re
input = open("in", "r").read()

x = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", input)

ans2 = 0
enabled = True

for m in x:
    if m == "do()":
        enabled = True
    elif m == "don't()":
        enabled = False
    elif len(m) > 0:
        vals = m.split(',') 
        a = vals[0][4:]
        b = vals[1][:-1]
        if enabled:
            ans2 += int(a) * int(b)

print(ans2)
