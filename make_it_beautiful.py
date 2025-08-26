from collections import Counter
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))

    lst.sort()
    min_ele = lst[0]
    max_ele = lst[n-1]

    res = []

    if min_ele == max_ele:
        print("NO")
    else:
        res.append(max_ele)
        for i in range(n-1):
            res.append(lst[i])
        print("YES")
        print(*res)











