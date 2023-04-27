# a, b = map(int, input().split())
n, m = map(int, input().split())
ln = []
for i in range(n):
    ln.append(0)

for index in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i, j + 1):
        ln[idx - 1] = k

for index in ln:
    print(ln[index], end = " ")