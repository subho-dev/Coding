#code
from itertools import combinations

#function to remove repeated sublists in a linst of sublists
def Remove(lst): 
     return ([list(i) for i in {*[tuple(sorted(i)) for i in lst]}])
     
#function to get all sublists from parent list
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs

#function to check the condition of the question
#Here sum of elements of a list should be equal to the number entered by user
def sublistspossible(arr,n,a):
    semifinal=[]
    final=[]
    # semifinal.clear()
    # final.clear()
    semifinal=sub_lists(arr)
    p=len(semifinal)
    for i in range(0,p,1):
        if(sum(semifinal[i])==a):
            final.append(semifinal[i])
        else:
            pass
    if len(final)==0:
        final.append("Empty")
    return final

#function to print the result in a proper sequence as accepted in the terminal
def printelements(e):
    count=0
    if e!="Empty":
        ans="("
        for i in (e):
            count+=1
            if count==len(e):
                ans+=str(i)
            else:
                ans+=str(i)+" "
        ans=ans+")"    
        return ans
    else:
        ans="Empty"
        return ans
    
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        arr.sort()
        a=int(input())
        ans=sublistspossible(arr,n,a)
        if ans[0]!="Empty":
            ans=Remove(ans)
            ans.sort()              #sorting the sublists inside the list in ascending order
        for i in ans:
            print(printelements(i),end="")
        print()
        ans.clear()
