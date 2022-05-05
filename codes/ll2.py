class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def printt(self):
        p=self.head
        while p is not None:
            print(p.data)
            p=p.next

list2=LL()
list2.head=Node(input())
for i in range(5):
    list2.lis.append()
e2=Node(int(input()))
e3=Node(int(input()))
list2.head.next=e2
e2.next=e3
list2.printt()
