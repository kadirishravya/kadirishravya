def cycle(self):
    if self.start is None and self.start.link is None:
        return
    slow=self.start
    fast=self.start
    while fast and fast.link:
        slow = slow.link
        fast = fast.link.link
        if fast==slow:
            return slow
        return None
def remove_cycle(self):
    c=self.cycle()
    if c is None:
        return
    p = c
    q = c
    cyc_length=0
    rem_len=0
    while True:
        cyc_length+=1
        p=p.link
        if p==q:
            break
    p=self.start
    while p!=q:
        rem_len+=1
        p=p.link
        q=q.link
    length_of_tot_list=cyc_length+rem_len
    print("the length of the list is",length_of_tot_list)

    p=self.start
    for i in range(length_of_tot_list-1):
        p=p.link
    p.link=None
