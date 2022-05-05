class BST:
    def __init__(self,info):
        self.info = info
        self.lchild = None
        self.rchild = None
class BST:
    def __init__(self):
        self.root=None

    def search(self,x):
        return self._search(self.root,x) is not None
    def _search(self,p,x):
        if p is None:
            return None
        if x<p.info:
            return self._search(p.lchild,x)
        if x>p.info:
            return self._search(p.rchild,x)
        return p

    def nonRec_search(self,x):
        p=self.root
        if p is None:
            return None
        while p is not None:
            if x<p.info:
                p=p.lchild
            elif x>p.info:
                p=p.rchild
            else:return True
        return False

    def min_val(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        p=self.root
        while p.lchild is not None:
            p=p.lchild
        return p.info

    def max_val(self):
        if self.is_empty():
            raise TreeEmptyError("the tree is empty")
        p=self.root
        while p.rchild is not None:
            p=p.right
        return p.info

    def insert(self,x):
        p=self.root
        parent=None
        while p is not None:
            if x<p.info:
                p=p.lchild
            elif x>p.info:
                p=p.rchild
            else:
                print("the value is already present")
                return
        temp=Node(x)
        if parent==None:
            self.root=temp
        elif x<parent.info:
            parent.lchild=temp
        else:
            parent.rchild=temp

    def insert_rec(self,x):
        self.root=self._insert_rec(self.root,x)
    def _insert_rec(self,p,x):
        if p is None:
            p=Node(x)
        elif x<p.info:
            p.lchild=self._insert_rec(p.lchild,x)
        elif x>p.info:
            p.rchild=self._insert_rec(p.rchild,x)
        else:print("The node is already present")
        return p
    # return p
    def deletion(self):
        


    
