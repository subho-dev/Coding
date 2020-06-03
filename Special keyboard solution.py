#code
def ans(n):
    if n < 5:
        return n
    return max(4*ans(n-5), 3*ans(n-4))
    
t=int(input())
while t!=0:
    a=int(input())
    print(ans(a))
    t-=1
