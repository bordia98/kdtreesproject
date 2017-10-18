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

    #this will insert node at root and else part will insert things at the branch
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

    # This is the function which is used to calculate the dimension
    #like we have consider in 2 dimension so we will find height using it
    def findheight(self,node):
        count=1
        while node.parent:
            count+=1
            node=node.parent
        return count

    # Other function to insert in 2 different dimension
    def insertbranch(self,node1,node):
        height=self.findheight(node1)%2
        if height==1:                                   #height==1 corresponds to x dimension and height = 0 corresponds to y direction
            if node.point[0]<node1.point[0]:            #point[0] as defind in the structure of the node means x coordinate and point[1] corresponds to y coordinate
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

    #printing the tree which is created printing is done in inorder traversals
    def printkdtree(self,node):
        if self.root==None:
            print("There is nothing to print")
        print(node.point,end='      ')
        if node.left !=None:
            self.printkdtree(node.left)
        if node.right!=None:
            self.printkdtree(node.right)

    # This code is to remove the node thing when we want to search via recursion and check the points
    def searchtree(self,x,y):
        if self.root==None:
            print("No match found")
        elif self.root.point[0]==x and self.root.point[1]==y:
            print("Match found")
        elif x<self.root.point[0]:
            self.searchtree_(x,y,self.root)
        elif x>=self.root.point[1]:
            self.searchtree_(x,y,self.root)

    # Search In KD Trees with the use of 3 parameters one is x coordinatre other is y coordinate and one is node in order to made recurssion

    def searchtree_(self,x,y,node):
        if node==None:
            print()
            print("No match found")
        elif node!=None:
            if node.point[0]==x and node.point[1]==y:
                print()
                print("Point is present in the tree")
                return True
            else:
                height=self.findheight(node)%2
                if height==1:
                    if x<node.point[0]:
                        if node.left!=None:
                            self.searchtree_(x,y,node.left)
                        else:
                            print()
                            print("No match found")
                            return False
                    if x>=node.point[0]:
                        if node.right!=None:
                            self.searchtree_(x,y,node.right)
                        else:
                            print()
                            print("No match found")
                            return False
                elif height==0:
                    if y<node.point[1]:
                        if node.left!=None:
                            self.searchtree_(x,y,node.left)
                        else:
                            print()
                            print("No match found")
                            return False
                    if y>=node.point[1]:
                        if node.right!=None:
                            self.searchtree_(x,y,node.right)
                        else:
                            print()
                            print("No match found")
                            return False



kd=kdtree()
kd.insert(6,8)
kd.insert(3,4)
kd.insert(5,6)
kd.insert(4,2)
kd.insert(8,9)
kd.insert(9,4)
kd.insert(9,10)
kd.printkdtree(kd.root)
kd.searchtree(4,2)