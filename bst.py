""" bst.py

Student: Nils Wikström
Mail: nils.wikstrom@outlook.com
Reviewed by: Sergi Olives juan
Date reviewed: 2022-05-12
"""


from linked_list import LinkedList
import random
import math

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        r = self.root
        return self._height(r)
    
    def _height(self,r):

        if r is None:
            return 0
        
        right = self._height(r.right)
        left = self._height(r.left)
        return max(right,left) + 1

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k) #left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right,k) #right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                temp = r.right
                while temp.left:
                    temp = temp.left
                k = temp.key
                r.key = k
                r.right = self._remove(r.right,k)
                
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                            # Compulsory
        n = 0
        ret = '<'
        for i in self.__iter__(): #Iterate over all elements
            if n == self.size()-1: #If last element add bracket
                ret = ret + str(i)
            else:                   #else add comma
                ret = ret + str(i) + ', '
            n = n + 1               #keep count
        return ret + '>'                  #return complete string



    def to_list(self):                            # Compulsory'
        lst = [] #create empty list
        for i in self.__iter__(): #iterate over tree
            lst.append(i)         #add each elemt to list
        return lst                #return list
                                    #Complexity: n                                

    def to_LinkedList(self):                      # Compulsory
        lst = LinkedList()                         #Same as above but linkedlist
        for i in self.__iter__():
            lst.insert(i)
        return lst                  #Complexity: n*complexity(insert) (n^2)

    def ipl(self):                                # Compulsory
        r = self.root
        level = 0

        return self._ipl(r,level)
    
    def _ipl(self,r,level):
        level = level +1 #keep track of level
        if r is None:   #if bottom return 0
            return 0
        return level + self._ipl(r.left,level) + self._ipl(r.right,level) 
        # return this level and add the level of both left and right

        



def random_tree(n):                               # Useful
    tree = BST()
    for i in range(n):
        tree.insert(random.random())
    return tree


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    tree1 = random_tree(100)
    tree2 = random_tree(1000)
    tree3 = random_tree(10000)

    print(tree1.ipl()/100)
    print(tree1.height())
    print(1.39*math.log(100,2))
    print()
    print(tree2.ipl()/1000)
    print(tree2.height())
    print(1.39*math.log(1000,2))
    print()
    print(tree3.ipl()/10000)
    print(tree3.height())
    print(1.39*math.log(10000,2))
    

    #21
    # SIZE: YES
    # HEIGHT: NO
    # CONTAINS: YES
    # INSERT: NO, ONLY VALUES
    # REMOVE: NO, ONLY VALUES




if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? 
2. computing height?
3. contains?
4. insert?
5. remove?




Results for ipl of random trees
===============================






"""
