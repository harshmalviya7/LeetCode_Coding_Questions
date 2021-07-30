# cook your dish here
# Permutation Cycles
# https://www.codechef.com/problems/PCYCLE
n = input()
l = list(map(int, input().split()))
res = []
for i in range(1, len(l) + 1):
    if l[i - 1] == 0:
        continue
    block = i
    current = i
    a = []
    while (True):
        a.append(current)
        current = l[current - 1]
        l[block - 1] = 0
        block = current
        if current == i:
            a.append(current)
            break

    res.append(a)
print(len(res))

for i in res:
    print(" ".join(str(j) for j in i))




