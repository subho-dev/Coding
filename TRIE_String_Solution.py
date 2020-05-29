#code
l=[]
ans=[]
t=int(input())
while t!=0:
    N=int(input())
    l=input().split(' ')
    A=input()
    
    for j in range(0,N,1):
        if A==l[j]:
            print(1)
            break
        else:
            if j==N-1:
                print(0)
            else:
                pass
    t=t-1
