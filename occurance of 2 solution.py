#User function Template for python3
def numberOf2sinRange(n):
    ans=0
    for i in range(1,n+1,1):
        ans+=str(i).count('2')
    return ans


if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))
