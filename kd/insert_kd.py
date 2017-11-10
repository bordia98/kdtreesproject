import sys
class treenode:
    def __init__(self):
        self.point=[]
        self.left=None
        self.right=None
        self.parent=None
global k
b=treenode()
c=treenode()
class kdtree:
    def __init__(self):
        self.root=None

    def newnode(self,a):
        temp=treenode()
        for i in range(k):
            temp.point.append(a[i])
        return temp
    def insert(self,coord):  #then add coord in the main and pass as argument
        a=list()
        for point in coord:
            a.append(point)
        temp=self.newnode(a)
        for i in range(k):
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
        height=(self.findheight(node1)-1)%k
        for i in range(k):
            if height==i:
                if node.point[i]<node1.point[i]:
                    if node1.left!=None:
                        self.insertbranch(node1.left,node)
                    else:
                        node1.left=node
                        node.parent=node1
                if node.point[i]>=node1.point[i]:
                    if node1.right!=None:
                        self.insertbranch(node1.right,node)
                    else:
                        node1.right=node
                        node.parent=node1
    def printkdtree(self,node):
        if self.root==None:
            print("There is nothing to print")
        k=node.point[0]
        print(node.point,end='      ')
        if node.left !=None:
            self.printkdtree(node.left)
        if node.right!=None:
            self.printkdtree(node.right)
kd=kdtree()
k=8
#k=(int)(input("enter the dimension of tree"))
for i in range(k):
    b.point.append(sys.maxsize)
    c.point.append(sys.maxsize)
#coordinates=[]
#counter=1
#while counter!=0:
#    for i in range(k):
 #       coordinates.append((int)(input("enter the co-ordinate")))
 #   kd.insert(coordinates)
kd.insert([3,6,0,0,0,0,0,0])
kd.insert([2,7,0,0,0,0,0,0])
kd.insert([17,15,3,0,0,0,0,0])
kd.insert([13,15,0,0,0,0,0,0])
#    counter=(int)(input("enter 0 to exit else to continue"))
kd.printkdtree(kd.root)
