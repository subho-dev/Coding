if __name__ == '__main__':
    res=[]
    t=int(input())
    for _ in range(t):
        a=input()
        v=list(a)
        n=len(v)
        ac=0
        bc=0
        cc=0
        for i in range(n):
	        ch = v[i]
	        if ch == 'a': ac = 1 + 2*ac
	        elif ch == 'b': bc = ac + 2*bc
	        elif ch == 'c': cc = bc + 2*cc
        print(cc)
