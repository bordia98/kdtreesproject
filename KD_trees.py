class treenode:
    def __init__(self):
        self.point=[]
        self.left=None
        self.right=None
        self.parent=None
global b
b=treenode()
global c
b.point.append(10000000)
b.point.append(10000000)
c=treenode()
c.point.append(10000000)
c.point.append(10000000)

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
        k=node.point[0]
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

    #method to find minimum in both x and y direction we have to start from the root in order to find the minimum

    def minimum(self,dimension):
        if self.root==None:
            print("There is nothing to find minimum")
        else:
            return self.minimum_(self.root,dimension,1) #this is done in order that the initial height is 1

    def minimum_(self,node,dimension,depth):
        global b, c
        if dimension=='x':
            z=0                 #x corresponds to the dimension with point index as 0
        elif dimension=='y':
            z=1                 # y corresponds to the dimension with point index as 1

        h=depth%2               #checking in which dimension we are currently working

        #after this use pycharm debugger to understand what i have done as i cant explain in comments :-p
        if h!=z:
            if node.left==None:
                t=node.point[z]
                return node
            return  self.minimum_(node.left,dimension,depth+1)

        a=node
        if node.left!=None:
            b=self.minimum_(node.left,dimension,depth+1)

        if node.right!=None:
            c=self.minimum_(node.right,dimension,depth+1)

        return self.minnode(a,b,c,z)

    def minnode(self,a,b,c,z):
        res=a
        if b!=None and b.point[z]<res.point[z]:
            res=b
        if c!=None and c.point[z]<res.point[z]:
            res=c
        return  res
    #method to find the maximum of the all

    def maximum(self,dimension):
        if self.root==None:
            print("There is nothing to find minimum")
        else:
            return self.maximum_(self.root,dimension,1) #this is done in order that the initial height is 1

    def maximum_(self,node,dimension,depth):
        if dimension=='x':
            z=0                 #x corresponds to the dimension with point index as 0
        elif dimension=='y':
            z=1                 # y corresponds to the dimension with point index as 1

        h=depth%2               #checking in which dimension we are currently working

        #after this use pycharm debugger to understand what i have done as i cant explain in comments :-p
        if h!=z:
            if node.right==None:
                t=node.point[z]
                return node.point[z]
            return  self.maximum_(node.right,dimension,depth+1)

        a=node.point[z]
        if node.left!=None:
            b=self.maximum_(node.left,dimension,depth+1)
        else:
            b=-10000000
        if node.right!=None:
            c=self.maximum_(node.right,dimension,depth+1)
        else:
            c=-10000000
        return max(a,b,c)

    #check whether the points are same or not
    def samepoints(self,a,b):
        for i in range(len(b)):
            if a[i]!=b[i]:
                return False
        return True

    #copy one point to another
    def copypoints(self,a,b):
        for i in range(len(a)):
            a[i]=b[i]

    #function of deleting node
    def deletenode(self,node,a,height):
        if node==None:
            return None

        flag=0
        h=height%2
        if h==1:
            z=0
            k='x'
        else:
            z=1
            k='y'

        if self.samepoints(node.point,a):
            flag=1
            if node.right!=None:
                minnode = self.minimum_(node.right,k,height)
                self.copypoints(node.point,minnode.point)
                node.right=self.deletenode(node.right,minnode.point,height+1)
            elif node.left!=None:
                minnode=self.minimum_(node.left,k,height)
                self.copypoints(node.point,minnode.point)
                node.right=self.deletenode(node.left,minnode.point,height+1)
            else:
                if node.parent.left==node:
                    node.parent.left=None
                else:
                    node.parent.right=None
                node.parent=None
                return None
            return node

        if a[z]<node.point[z]:
            node.left=self.deletenode(node.left,a,height+1)
        else:
            node.right=self.deletenode(node.right,a,height+1)

        return node

    #wrapping function for deleting node
    def deletekdnode(self,a):
        return self.deletenode(self.root,a,1)


def main():
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
    print("The minimum in x direction  is ",kd.minimum('x').point[0])
    print("The minimum in y direction is " , kd.minimum('y').point[1])
    print("The maximum in x direction is " , kd.maximum('x'))
    print("The maximum in y direction is " , kd.maximum('y'))
    a=[5,6]
    kd.deletekdnode(a)
    kd.printkdtree(kd.root)
    a=[3,4]
    kd.deletekdnode(a)
    print()
    kd.printkdtree(kd.root)
    print()
    a=[100,50]
    w=kd.deletekdnode(a)
    kd.printkdtree(kd.root)
if __name__=='__main__':
    main()
