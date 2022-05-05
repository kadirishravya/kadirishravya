#print(*"hello , world".split()[::-1],sep=" ")
# s="shr"+"."+"\n"+"avya"
# print(s,"s"+"2")
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self,ex):
        self.head=None
        self.ex=ex
    def pr(self,ex):
        p=self.head
        while p!=None:
            if p.data == ex:
                print(p.data)
            p=p.next

list1=LL(2)
list1.head=Node(int(input()))
e2=Node(int(input()))
e3=Node(int(input()))
list1.head.next=e2
e2.next=e3
list1.pr(2)
print()
