for _ in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    res = 0

    if n > 1:
        for i in range(1, n):
            if lst[i] % 2 == lst[i - 1] % 2:
                res += 1

    print(res)
