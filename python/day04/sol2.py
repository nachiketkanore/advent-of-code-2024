mat = [line for line in open('in', 'r').read().split('\n') if len(line) > 0]
N, M = len(mat), len(mat[0])


ans = 0
for i in range(1,N-1):
    for j in range(1,M-1):
        a = mat[i - 1][j - 1] + mat[i][j] + mat[i + 1][j + 1]
        b = mat[i + 1][j - 1] + mat[i][j] + mat[i - 1][j + 1]
        if (a == "MAS" or a == "SAM") and (b == "MAS" or b== "SAM"):
            ans += 1
print(ans)
