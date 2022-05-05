class Node:
    def __init__(self,info):
        self.info=info
        self.link=None
class BubLL:
    def __init__(self):
        self.start=None

    def bub_sort_data(self):
        end =None
        while end!=self.start.next:
            p=self.start
            while p.next!=end:
                q=p.next
                if p.info>q.info:
                    p.info,q.info=q.info,p.info
                p=p.next
            end=p

    def bub_sort_linkEX(self):
        end=None
        while end!=self.start.next:
            r=p=self.start
            while p.next!=end:
                q=p.next
                if p.info>q.info:
                    p.next=q.next
                    q.next=p
                    if p!=self.start:
                        r.next=q
                    else:
                        self.start=q
                    p,q=q,p
                r=p
                p=p.next
            end=p

obj
