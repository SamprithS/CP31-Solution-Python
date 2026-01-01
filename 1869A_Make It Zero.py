for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if n%2 == 0:
        print("2")
        print(f"1 {n}")
        print(f"1 {n}")
    else:
        print("4")
        print(f"1 {n-1}")
        print(f"1 {n - 1}")
        print(f"{n-1} {n}")
        print(f"{n-1} {n}")
