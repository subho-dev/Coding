for _ in range(int(input())):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    H = [0]*(n+m-1)
    for i in range(n):
        for j in range(m):
            H[(n-i-1)+(m-j-1)] += arr[i]*brr[j]
    H = H[::-1]
    print(*H)
