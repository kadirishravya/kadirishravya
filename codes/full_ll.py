class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None

    def inserting_begi(self,data):
        temp=Node(data)
        temp.link=self.head
        self.head=temp

    def insert_end(self,data):
        temp=Node(data)
        while self.head is None:
            self.head=temp
            return
        p=self.head
        while p is not None:
            p=p.next
        p.next=temp

    def insert_after(self,x,data):
        #temp=Node(data)
        p=self.head
        while p is not None:
            if p.data==x:
                break
            p=p.next
        if self.head is None:
            print("there is no such ele in list")
        else:
            temp=Node(data)
            temp.next=p.next
            p.next=temp
            lobj.printLis()

    def insert_before(self,x,data):
        if self.head==None:
            print("list is empty")

        if self.head.data==x:
            temp=Node(data)
            temp.next=self.head
            self.head=temp
        temp=Node(data)
        p=self.head
        while p.next is not None:
            if p.next.data==x:
                break
            p=p.next
        if p.next is None:
            print(x,"is not present in the list")
        else:
            temp.next=p.next
            p.next=temp
            lobj.printLis()


    def insert_pos(self,x,data):
        if x==1:
            temp=Node(data)
            temp.next=self.head
            self.head=temp
            return

        p=self.head
        i=1
        if i<x-1 and p is not None:
            p=p.next
            i+=1
        if p is None:
            print(x," is not present in the list")
        else:
            temp=Node(data)
            temp.next=p.next
            p.next = temp

    def deletion_1st(self):
        if self.head is None:
            print("the list  is empty")
            return
        self.head=self.head.next

    def deletion_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
            return
        p=self.head
        while p.next.next is not None:
            p=p.next
        p.next=None

    def delete_node(self,x):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data==x:
            self.head=self.head.next
            return
        p=self.head
        while p.next is not None:
            if p.next.data==x:
                break
            p=p.next
        if p.next is None:
            print("the ele is not exist ",x)
        else:
            p.next=p.next.next



    def countinglis(self):
        temp=self.head
        c=0
        if self.head is None:
            print("there are no values in the linked list")
        while temp:
            c+=1
            temp=temp.next
        print("the no.of nodes in the linked list is ",c)


    def search_ele(self,x):
        pos=1
        temp=self.head
        while temp:
            if x==temp.data:
                print("the given ele is in position ",x)
                return True
            pos+=1
            temp=temp.next
        else:
            print(x ,"not found in the list")
            return False

    def bub_sort_data(self):
        end = None
        while end != self.head.next:
            p = self.head
            while p.next != end:
                q = p.next
                if p.data > q.data:
                    p.data, q.data = q.data, p.data
                p = p.next
            end = p

    def bub_sort_linkEX(self):
        end=None
        while end!=self.head.next:
            r=p=self.head
            while p.next!=end:
                q=p.next
                if p.data>q.data:
                    p.next=q.next
                    q.next=p
                    if p!=self.head:
                        r.next=q
                    else:
                        self.head=q
                    p,q=q,p
                r=p
                p=p.next
            end=p

    def printLis(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

lobj=Linked_list()
lobj.head=Node(1)
sce=Node(2)
third=Node(3)
lobj.head.next=sce
sce.next=third
third.next=None
print("big 1st")
lobj.printLis()
lobj.countinglis()
print("-----------------")
lobj.inserting_begi(53)
lobj.insert_after(53,106)
lobj.insert_before(53,155)
print("after inserting")
#lobj.insert_end(110)
lobj.printLis()
#lobj.deletion_last_node()
lobj.delete_node(155)
print("-----")
lobj.bub_sort_data()
lobj.printLis()
lobj.bub_sort_linkEX()
print("_______")
lobj.printLis()
lobj.countinglis()

lobj.search_ele(155)


