import heapq
class pq:
    def __init__(self):
        pass
    def create(self,arr):
        heapq.heapify(arr)
        l=list()
        while arr:
            l.append(heapq.heappop(arr))
        return l[::-1]
    def push(self,arr,n):
        temp=list()
        for i in arr:
            if n>i:
                temp.append(n)
                n=float('-inf') #Changing the value to minimum possible value
                temp.append(i)
            elif n<i:
                temp.append(i)
        return temp
    def pop(self,arr):
        return(arr.pop(0))
        
        
#Driver Code
arr=[int(x) for x in input().split(' ')]
obj=pq()
arr=obj.create(arr)     #Priority Queue Creation
arr=obj.push(arr,102)   #Pushing values into Priority Queue
print(*arr)
arr=obj.push(arr,5)     #Pushing values into Priority Queue
print(*arr)
print(obj.pop(arr))     #Popping values from Priority Queue
