import random
import sys


class treenode:
    def __init__(self):                 #initializing treenode
        self.point = []
        self.left = None
        self.right = None
        self.parent = None


class kdtree:
    def __init__(self, k):
        self.k = k                  #for using k dimension all over
        self.root = None

    def newnode(self, a):           #for creating newnode everytime
        temp = treenode()
        for i in range(self.k):
            temp.point.append(a[i])
        return temp

    #insert function using list is passed as the parameters
    def insert(self, coord):
        a = list()
        for point in coord:
            a.append(point)
        temp = self.newnode(a)
        for i in range(self.k):
            a.pop()
        if self.root == None:
            self.root = temp
        else:
            self.insertbranch(self.root, temp)      #calling of adjacent function

    #function to calculate the height of each node in order to tract the dimension
    def findheight(self, node):
        count = 1
        while node.parent:
            count += 1
            node = node.parent
        return count

    #extension function of insert
    def insertbranch(self, node1, node):
        height = (self.findheight(node1) - 1) % self.k  #knowing the dimension
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

    # printing the tree which is created printing is done in preorder traversals
    def printkdtree(self, node):
        if self.root == None:
            print("There is nothing to print")
        y = node.point[0]
        print(node.point, end='      ')
        if node.left != None:
            self.printkdtree(node.left)
        if node.right != None:
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

    #function to check the data in node are same or not
    def checksame(self, node, a):
        for i in range(len(a)):
            if node.point[i] != a[i]:
                return False
        return True

    # Search In KD Trees with the use of 2 parameters one is list and one is node in order to made recurssion

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
                print(self.findheight(node))
                height = (self.findheight(node) - 1) % self.k
                if a[height] < node.point[height]:
                    if node.left != None:
                        self.searchtree_(a, node.left)
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

    #function to find the minimum of any dimension paramenter requirement is dimension number
    def minimum(self, dimension):
        if self.root == None:
            print("There is nothing to find minimum")
        else:
            return self.minimum_(self.root, dimension, 0)  # this is done in order that the initial height is 0

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
            b = None

        if node.right != None:
            c = self.minimum_(node.right, dimension, depth + 1)
        else:
            c = None

        return self.minnode(a, b, c, z)

    #finding the minimum of three node
    def minnode(self, a, b, c, z):
        res = a
        if b == None:
            b = treenode()
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

    # method to find the maximum of the all

    def maximum(self, dimension):
        if self.root == None:
            print("There is nothing to find minimum")
        else:
            return self.maximum_(self.root, dimension, 0)  # this is done in order that the initial height is 1

    def maximum_(self, node, dimension, depth):
        z = dimension
        h = depth % self.k  # checking in which dimension we are currently working

        h = depth % 2  # checking in which dimension we are currently working

        # after this use pycharm debugger to understand what i have done as i cant explain in comments :-p
        if h == z:
            if node.right == None:
                t = node.point[z]
                return node.point[z]
            return self.maximum_(node.right, dimension, depth + 1)

        a = node.point[z]
        if node.left != None:
            e = self.maximum_(node.left, dimension, depth + 1)
        else:
            e = -10000000
        if node.right != None:
            f = self.maximum_(node.right, dimension, depth + 1)
        else:
            f = -10000000
        return max(e, f, a)

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
                minnode = self.minimum_(node.right, h, height + 1)
                self.copypoints(node.point, minnode.point)
                node.right = self.deletenode(node.right, minnode.point, height + 1)
            elif node.left != None:
                minnode = self.minimum_(node.left, h, height + 1)
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


def main():
    print("Enter the value of k in which you waant to run data Structure")
    k = int(input())
    kd = kdtree(k)

    a = list()
    z = True

    for i in range(10):
        for i in range(k):
            rand = random.randint(0, 60)
            a.append(rand)
        kd.insert(a)
        a = []
    kd.printkdtree(kd.root)
    print()
    z = True
    while z:
        print("Enter the coordinates you want to check in the tree are present or not")
        a = list((map(int, input().split(" "))))
        kd.searchtree(a)
        a = []
        print("Io end entering data press 0 to continue enter anything")
        u = int(input())
        if u == 0:
            z = False
    z = True
    while z:
        print("The minimum in selected direction is ")
        a = int(input())
        t = kd.minimum(a).point[a]
        a = []
        print(t)
        print("Io end entering data press 0 to continue enter anything")
        u = int(input())
        if u == 0:
            z = False
    z = True
    while z:
        print("The maximum in selected direction is ")
        a = int(input())
        t = kd.maximum(a)
        a = []
        print(t)
        print("Io end entering data press 0 to continue enter anything")
        u = int(input())
        if u == 0:
            z = False
    z = True
    while z:
        print("Enter the coordinates of the node you want to delete")
        a = list(map(int, input().split()))
        t = kd.deletekdnode(a)
        a = []
        kd.printkdtree(kd.root)
        print()
        print("Io end entering data press 0 to continue enter anything")
        u = int(input())
        if u == 0:
            z = False


if __name__ == '__main__':
    main()
