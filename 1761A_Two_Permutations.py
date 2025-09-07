for _ in range(int(input())):
    n, a, b = map(int, input().split())

    if (a+b+2 <= n) or (a == b and a == n):
        print("YES")
    else:
        print("NO")
