from collections import deque
class Node:
    def __init__(self,info):
        self.info = info
        self.lchild = None
        self.rchild = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def preorder_traversal(self):
        self._preorder_traversal(self.root)
        print()

    def _preorder_traversal(self,p):
        if p in None:
            return
        print(p.info,' ',end='')
        self._preorder_traversal(p.lchild)
        self._preorder_traversal(p.rchild)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()

    def _inorder_traversal(self,p):
        if p is None:
            return None
        self._inorder_traversal(p.lchild)
        print(p.info,' ',end='')
        self._preorder_traversal(p.rchild)

    def postorder_traversal(self):
        self._postorder_traversal(self.root)
        print()

    def _postorder_traversal(self,p):
        if p is None:
            return
        self._postorder_traversal(p.rchild)
        self._postorder_traversal(p.lchild)
        print(p.info," ",end='')

    def create_tree(self):
        self.root=Node('A')
        self.root.lchild=Node('B')
        self.root.rchild=Node('C')
        self.root.lchild.lchild=Node('D')
        self.root.lchild.rchild=Node('E')
        self.root.rchild.lchild=Node('F')
        self.root.rchild.rchild=Node('G')

    def level_order_trav(self):
        if self.root is None:
            print("tree is empty")
            return
        qu=deque()
        qu.append(self.root)

        while len(qu)!=0:
            p=qu.popleft()
            print(p.info+' ',end='')
            if p.lchild is not None:
                qu.append(p.lchild)
            if p.rchild is not None:
                qu.append(p.rchild)