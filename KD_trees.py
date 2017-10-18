class treenode:
    def __init__(self):
        self.point=[]
        self.left=None
        self.right=None
        self.parent=None

class kdtree:
    def __init__(self):
        self.root=None

    def newnode(self,a):
        temp=treenode()
        for i in range(2):
            temp.point.append(a[i])
        return temp

    def insert(self,x,y):
        a=list()
        a.append(x)
        a.append(y)
        temp=self.newnode(a)
        a.pop()
        a.pop()
        if self.root==None:
            self.root=temp
        else:
            self.insertbranch(self.root,temp)

    def findheight(self,node):
        count=1
        while node.parent:
            count+=1
            node=node.parent
        return count

    def insertbranch(self,node1,node):
        height=self.findheight(node1)%2
        if height==1:
            if node.point[0]<node1.point[0]:
                if node1.left!=None:
                    self.insertbranch(node1.left,node)
                else:
                    node1.left=node
                    node.parent=node1
            if node.point[0]>=node1.point[0]:
                if node1.right!=None:
                    self.insertbranch(node1.right,node)
                else:
                    node1.right=node
                    node.parent=node1
        elif height==0:
            if node.point[1]<node1.point[1] :
                if node1.left!=None:
                    self.insertbranch(node1.left,node)
                else:
                    node1.left=node
                    node.parent=node1
            if node.point[1]>=node1.point[1]:
                if node1.right!=None:
                    self.insertbranch(node1.right,node)
                else:
                    node1.right=node
                    node.parent=node1

    def printkdtree(self,node):
        if self.root==None:
            print("There is nothing to print")
        print(node.point)
        if node.left !=None:
            self.printkdtree(node.left)
        if node.right!=None:
            self.printkdtree(node.right)

kd=kdtree()
kd.insert(6,8)
kd.insert(3,4)
kd.insert(5,6)
kd.insert(4,2)
kd.insert(8,9)
kd.insert(9,4)
kd.insert(9,10)
kd.printkdtree(kd.root)