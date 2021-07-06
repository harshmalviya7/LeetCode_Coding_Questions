# 1338. Reduce Array Size to The Half
# https://leetcode.com/problems/reduce-array-size-to-the-half/

def minSetSize(self, arr: List[int]) -> int:
    d = defaultdict(int)
    for i in arr:
        d[i] += 1
    a = [v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)]
    print(a)
    n = len(arr)
    i = 0

    while (n > len(arr) // 2):
        n -= a[i]
        i += 1

    return i