
def sort012(arr,n):
    # code here
    arr.sort()
    
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sort012(arr,n)
        k=int(input())
        print(arr[k-1])

