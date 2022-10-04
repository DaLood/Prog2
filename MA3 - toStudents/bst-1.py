""" bst.py

Student: David Lood
Mail: david.lood.3070@student.uu.se
Reviewed by: Xiaoxia Liu
Date reviewed: 28/9
"""
import random
import math

from linked_list import LinkedList



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
    def insert(self, key):      # Not compulsory
        f = self.root
        if f is None:
            self.root = self.Node(key)
            return self.root

        while f:
            if key == f.key:
                break
            elif key < f.key:
                if f.left is None:
                    f.left = self.Node(key)
                    break
                else:
                    f = f.left
            elif key > f.key:
                if f.right is None:
                    f.right = self.Node(key)
                    break
                else:
                    f = f.right


    def contains(self, k):               # Not compulsory
        return self._contains(self.root, k)
    def _contains(self, f, k):
        if f is None:
            return False
        elif f.key == k:
            return True
        elif k < f.key:
            return self._contains(f.left,k)
        elif k > f.key:
            return self._contains(f.right,k)





    def height(self):               # Compulsory
        return self._height(self.root)

    def _height(self,f):
        if f is None:
            return 0
        else:
            return 1 + max(self._height(f.left), self._height(f.right))




    def remove(self, key):                 # Compulsory
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)
            # r.left = left subtree with k removed
        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.
                # Find the smallest key in the right subtree
                temp = r.right
                minimum = temp.key
                while temp.left:
                    temp = temp.left
                    minimum = temp.key
                # Put that key in this node
                r.key = minimum
                # Remove that key from the right subtree
                r.right  = self._remove(r.right, minimum)
        return r #Remember this! It applies to some of the cases above


    def __str__(self):  # Compulsory
        if self is None:
            return '<>'
        result_string = ('<')
        for i in self:
            result_string += ', ' + str(i)
        return result_string.replace('<, ','<',1) + '>'


    def to_list(self):          # Compulsory
        return [i for i in self]
    # komplexitet Theta(n) itererar över n element

    def to_LinkedList(self):                      # Compulsory
        lst = LinkedList()
        for i in self:
            lst.insert(i)
        return lst
    # Komplexitet Theta(n^2), iterar över n element, men instättningen itererar också över n element





    def level(self, f):          # Compulsory alternative 2
        if f is None:
            return 0
        return self._level(self.root, f)

    def _level(self, f, k):
        if f.key == k:
            return 1
        elif k < f.key:
            return 1 + self._level(f.left, k)
        elif k > f.key:
            return 1 + self._level(f.right, k)


    def ipl(self):
        res =  0
        for i in self:
            res += self.level(i)
        return res







def random_tree(n):                               # Useful
    t = BST()
    for i in range(n):
        t.insert(random.random())
    return t



def main():

    t = BST()
    for x in [12,5,2,8,7,23,17,36,13,21,42,25]:
        t.insert(x)
    t.remove(24)
    print(t)

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")



    # import matplotlib.pyplot as plt
    # res1 = []
    # res2 = []
    # res3 = []
    # x = range(1,4000)

    # for i in x:
    #     t = random_tree(i)
    #     res1.append(1.39*math.log2(i))
    #     res2.append(t.ipl()/t.size())
    #     res3.append(t.height())
    # plt.plot(x,res1, label = '1')
    # plt.plot(x, res2, label = '2')
    # plt.plot(x, res3, label = '3')
    # plt.legend
    # plt.savefig('plot.png')
    # plt.show()
    # res1 växer som res2 men sklijer med en konstant theta(1).
    # Så stor som höjden på trädet är ungefär 2.6 gånger så stor som den genomsnittliga nodhöjden.


    n = int(1e6)
    t1 = random_tree(n)

    h = t1.height()
    ipl_n = t1.ipl()/n

    print(1.39 * math.log2(n))
    print(f'n={n}, h={h}, IPL/n={ipl_n}')



if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size?
    Yes, do a counter that for every iteration adds 1.
    
2. computing height?
    No
    
3. contains?
    Yes goes through every node and if a node corresponds to the input return true otherwise return False

4. insert?
    No

5. remove?
    No


Results for ipl of random trees
===============================

n = 10
h = 6
IPL/n = 3.3
Teoretiskt: IPL/n = 1.39*log2(n) = 4.6



n = 100
h = 13
IPL/n = 7.38
Teoretiska: IPL/n = 1.39*log2(n) = 9.2



n = 1e3
h = 21
IPL/n = 12.04
Teoretiska: IPL/n = 1.39*log2(n) = 13.9



n = 1e4
h = 29
IPL/n = 16
Teoretiska: IPL/n = 1.39*log2(n) = 18.5


n = 1e5
h = 42
IPL/n = 21
Teoretiska: IPL/n = 1.39*log2(n) = 23.1
    
    
n = 1e6
h = 53
IPL/n = 27
Teoretiska: IPL/n = 1.39*log2(n) = 27.7


h ~= 2.6*Theta(log2(n))

h ~= 2.6*math.log2(1e5) ~= 42
h ~= 2.6*log2(1e6) ~= 53



"""
