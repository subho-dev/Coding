def compare(temp1, temp2):
    head1=temp1
    head2=temp2
    x=[]
    y=[]
    #return 1/-1/0
    while(temp1):
        x.append(temp1.data)
        temp1=temp1.next
    while(temp2):
        y.append(temp2.data)
        temp2=temp2.next
    if (x==y):
        return 0
    elif (x>y):
        return 1
    else:
        return -1




class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

        
    

        
def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=input().split()
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
            
        n2=int(input())
        arr2=input().split()
        ll2=Llist()
        tail=None
        for nodeData in arr2:
            tail=ll2.insert(nodeData,tail)
        
        
        print(compare(ll1.head,ll2.head))
        
    
    
# } Driver Code Ends
