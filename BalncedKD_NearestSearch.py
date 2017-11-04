import random
import sys,math
from svg import Circle,Rectangle,Scene,Line,Rectangle,Text
def colorstr(rgb): return "#%x%x%x" % (int(rgb[0]/16),int(rgb[1]/16),int(rgb[2]/16))
class treenode:
    def __init__(self):
        self.point=[]
        self.left=None
        self.right=None
        self.parent=None

class kdtree:
    def __init__(self,k):
        self.k=k
        self.root=None


    def newnode(self, a):
        temp = treenode()
        for i in range(self.k):
            temp.point.append(a[i])
        return temp

    def insert(self, coord):  # then add coord in the main and pass as argument
        a = list()
        for point in coord:
            a.append(point)
        temp = self.newnode(a)
        for i in range(self.k):
            a.pop()
        if self.root == None:
            self.root = temp
        else:
            self.insertbranch(self.root, temp)

    def findheight(self, node):
        count = 1
        while node.parent:
            count += 1
            node = node.parent
        return count

    def insertbranch(self, node1, node):
        height = (self.findheight(node1) - 1) % self.k
        for i in range(self.k):
            if height == i:
                if node.point[i] < node1.point[i]:
                    if node1.left != None:
                        self.insertbranch(node1.left, node)
                    else:
                        node1.left = node
                        node.parent = node1
                if node.point[i] >= node1.point[i]:
                    if node1.right != None:
                        self.insertbranch(node1.right, node)
                    else:
                        node1.right = node
                        node.parent = node1

    #printing the tree which is created printing is done in inorder traversals
    def printkdtree(self,node):
        if self.root==None:
            print("There is nothing to print")
        y=node.point[0]
        print(node.point,end='      ')
        if node.left !=None:
            self.printkdtree(node.left)
        if node.right!=None:
            self.printkdtree(node.right)

    # This code is to remove the node thing when we want to search via recursion and check the points
    def searchtree(self, a):
        if self.root == None:
            print("No match found")
        elif self.checksame(self.root, a):
            print("Match found")
        elif a[0] < self.root.point[0]:
            self.searchtree_(a, self.root.left)
        elif a[0] >= self.root.point[0]:
            self.searchtree_(a, self.root.right)


    def checksame(self, node, a):
        for i in range(len(a)):
            if node.point[i] != a[i]:
                return False
        return True

    # Search In KD Trees with the use of 3 parameters one is x coordinatre other is y coordinate and one is node in order to made recurssion

    def searchtree_(self, a, node):
        if node == None:
            print()
            print("No match found")
        elif node != None:
            if self.checksame(node, a):
                print()
                print("Point is present in the tree")
                return True
            else:
                height = (self.findheight(node)-1) % self.k
                if a[height] < node.point[height]:
                    if node.left != None:
                        self.searchtree_(a,node.left)
                    else:
                        print()
                        print("No match found")
                        return False
                if a[height] >= node.point[height]:
                    if node.right != None:
                        self.searchtree_(a, node.right)
                    else:
                        print()
                        print("No match found")
                        return False

    def minimum(self, dimension):
        if self.root == None:
            print("There is nothing to find minimum")
        else:
            return self.minimum_(self.root, dimension, 0)  # this is done in order that the initial height is 1

    def minimum_(self, node, dimension, depth):
        z = dimension
        h = depth % self.k  # checking in which dimension we are currently working

        # after this use pycharm debugger to understand what i have done as i cant explain in comments :-p
        if h == z:
            if node.left == None:
                t = node.point[z]
                return node
            return self.minimum_(node.left, dimension, depth + 1)

        a = node
        if node.left != None:
            b = self.minimum_(node.left, dimension, depth + 1)
        else:
            b=None

        if node.right != None:
            c = self.minimum_(node.right, dimension, depth + 1)
        else:
            c=None

        return self.minnode(a, b, c, z)

    def minnode(self, a, b, c, z):
        res = a
        if b == None:
            b=treenode()
            for i in range(self.k):
                b.point.append(sys.maxsize)
        if c == None:
            c = treenode()
            for i in range(self.k):
                c.point.append(sys.maxsize)
        if b.point[z] <= res.point[z]:
            res = b
        if c.point[z] <= res.point[z]:
            res = c
        return res

    #method to find the maximum of the all

    def maximum(self,dimension):
        if self.root==None:
            print("There is nothing to find minimum")
        else:
            return self.maximum_(self.root,dimension,0) #this is done in order that the initial height is 1

    def maximum_(self,node,dimension,depth):
        z = dimension
        h = depth % self.k  # checking in which dimension we are currently working

        h=depth%2               #checking in which dimension we are currently working

        #after this use pycharm debugger to understand what i have done as i cant explain in comments :-p
        if h==z:
            if node.right==None:
                t=node.point[z]
                return node.point[z]
            return  self.maximum_(node.right,dimension,depth+1)

        a=node.point[z]
        if node.left!=None:
            e=self.maximum_(node.left,dimension,depth+1)
        else:
            e=-10000000
        if node.right!=None:
            f=self.maximum_(node.right,dimension,depth+1)
        else:
            f=-10000000
        return max(e,f,a)

    def samepoints(self, a, b):
        for i in range(len(b)):
            if a[i] != b[i]:
                return False
        return True

        # copy one point to another

    def copypoints(self, a, b):
        for i in range(len(b)):
            a[i] = b[i]

            # function of deleting node

    def deletenode(self, node, a, height):
        if node == None:
            return None

        h = height % self.k
        if self.samepoints(node.point, a):
            if node.right != None:
                minnode = self.minimum_(node.right, h, height+1)
                self.copypoints(node.point, minnode.point)
                node.right = self.deletenode(node.right, minnode.point, height + 1)
            elif node.left != None:
                minnode = self.minimum_(node.left, h, height+1)
                self.copypoints(node.point, minnode.point)
                node.right = self.deletenode(node.left, minnode.point, height + 1)
            else:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
                node.parent = None
                return None
            return node

        if a[h] < node.point[h]:
            node.left = self.deletenode(node.left, a, height + 1)
        else:
            node.right = self.deletenode(node.right, a, height + 1)
        return node

    def deletekdnode(self, a):
        return self.deletenode(self.root, a, 0)

    def search_nearest(self,searchpoint):
        m=treenode()
        m=closest_point_perfect(self.root,searchpoint,0)
        return m.point

k=2
def distance(point1,point2):
    x1 , y1 = point1
    x2 , y2 = point2
    dx = x2-x1
    dy = y2-y1
    d = math.sqrt(dx*dx + dy*dy)
    return d

nextBest=treenode()
nextBranch=treenode()
oppositeBranch=treenode()

def closer(searchpoint,p1,p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1

    d1 = distance(p1.point,searchpoint)
    d2 = distance(p2.point,searchpoint)
    if d1 > d2:
        return p2
    return p1


def closest_point_perfect(root,searchpoint,depth): # Accurecy : 100%
    k=2
    if root is None:
        return None
    axis = depth % k
    if searchpoint[axis] < root.point[axis] :
        nextBranch=root.left
        oppositeBranch=root.right
    else:
        nextBranch=root.right
        oppositeBranch=root.left
    best = closer(searchpoint,closest_point_perfect(nextBranch,searchpoint,depth+1),root)
    if distance(best.point,searchpoint) > abs(root.point[axis]-searchpoint[axis]):
        best = closer(searchpoint,closest_point_perfect(oppositeBranch,searchpoint,depth+1),best)
    return best


def closest_point(root,best,searchpoint,depth):              #this function has less accurecy
    axis = depth % k
    if root is None:
        return best.point
    if best is None or distance(best.point,root.point)>distance(searchpoint,root.point):
        nextBest = root
    else:
        nextBest = best
    if searchpoint[axis] < root.point[axis]:
        nextBranch=root.left
        # oppositeBranch=root.right
    else:
        nextBranch=root.right
        # oppositeBranch=root.left
    # best=closer(nextBranch,oppositeBranch,searchpoint)

    return closest_point(nextBranch,nextBest,searchpoint,depth+1)


def main():
    print("Enter the value of k in which you waant to run data Structure")
    k = int(input())
    kd=kdtree(k)
    l=list()
    a=list()
    z=True
    scene = Scene('test')
    # scene.add(Rectangle((100,100),200,200,(255,255,255)))
    if k>0:
        for i in range(10):
            for i in range(k):
                rand= random.randint(100,300)
                a.append(rand)

        #kd.insert(a)
            if k==2:
                scene.add(Circle((a[0],a[1]),3,(0,255,0)))      #Adds circle when k=2
            l.append(a)
            a=[]
         #Testing nearest distance
        '''p=[]
        p=l
        x=[]
        for i in range(len(p)):
            x.append(distance(p[i],[100,100]))
        x.sort()
        print('List :',x[0])'''
        height = 0
        while len(l) > 0:
            axis = height % 2
            if height==0:
                h=1
            else:
                h = height ** 2
            while h > 0 and len(l) != 0:
                l = sorted(l, key=lambda point: point[axis])
                if (len(l) % 2 != 0):
                    n = (len(l) - 1) // 2
                    kd.insert(l[n])
                else:
                    n = (len(l) // 2) - 1
                    kd.insert(l[n])
                l.pop(n)
                h -= -1
            height += 1

        print("The kd tree in pre Order Traversal is ")
        kd.printkdtree(kd.root)
        print()

        print("Do you want to search coordinates in KD tree[y/n]?")
        ans=input()
        if ans=='y' or ans=='Y':
            z=True
            while z:
                print("Enter the coordinates you want to check in the tree are present or not")
                a=list((map(int,input().split(" "))))
                kd.searchtree(a)
                a=[]
                print("Io end entering data press 0 to continue enter anything")
                u = int(input())
                if u == 0:
                    z = False

        print("Do you want to find minimum of a given dimension[y/n]")
        ans=input()
        if ans=='y' or ans=='Y':
            z = True
            while z:
                print("The minimum in selected direction is ")
                a = int(input())
                if a>=0 and a<k:
                    t=kd.minimum(a).point[a]
                    a = []
                    print(t)
                    print("Io end entering data press 0 to continue enter anything")
                    u = int(input())
                    if u == 0:
                        z = False
                else:
                    print("Please enter the correct dimension")

        print("Do you want to find maximum of a given dimension[y/n]")
        ans=input()
        if ans=='y' or ans=='Y':
            z = True
            while z:
                print("The maximum in selected direction is ")
                a = int(input())
                if a>=0 and a<k:
                    t = kd.maximum(a)
                    a = []
                    print(t)
                    print("Io end entering data press 0 to continue enter anything")
                    u = int(input())
                    if u == 0:
                        z = False

        print("Do you want to delete any node from the created tree[y/n]")
        ans=input()
        if ans=='y' or ans=='Y':
            z = True
            while z:
                print("Enter the coordinates of the node you want to delete")
                a = list(map(int,input().split()))
                t = kd.deletekdnode(a)
                a = []
                kd.printkdtree(kd.root)
                print()
                print("Io end entering data press 0 to continue enter anything")
                u = int(input())
                if u == 0:
                    z = False

        #Nearest Neighbour search in Two dimension
        if k==2:
            print("Enter the point where you want to do the nearest search")
            p=[]
            p=list(map(int,input().split()))
            b=kd.search_nearest(p)
            print("The nearest Neighbour is present at the location ",b)
            print("The distance of the nearest neighbour is ",distance(p,b))
            scene.add(Circle((p[0],p[1]),3,(255,0,0)))
            scene.add(Circle((b[0],b[1]),3,(0,0,0)))
            #scene.display()
    else:
        print("Enter correct value of k")

if __name__=='__main__':
    main()
