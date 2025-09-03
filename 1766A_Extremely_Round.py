for _ in range(int(input())):
    n = int(input())
    cnt = 0

    while n >= 10:
        n = n//10
        cnt += 1

    print((cnt*9)+n)















