"""
Solutions to exam tasks for module 3.
Name:
Code:

The file contains:
   1) the class LinkedList with tasks A5, A6 and B2,
   2) the class BST with tasks A7, A8, 
   3) the function bst_sort to be analyzed in task B3
 

The main function runs a small test of the methods. Note that main will not
fully function until all tasks are solved.
"""
import random
import time
import math


class ExamException(Exception):
    def __init__(self, arg):
        self.arg = arg


class LinkedList:
    class Node:
        def __init__(self, data, succ=None):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __str__(self):
        return '(' + ', '.join([str(x) for x in self]) + ')'

    def add_last(self, x):
        """ Adds x at the end of the list """
        if self.first == None:
            self.first = self.Node(x)
        else:
            f = self.first
            while f.succ:
                f = f.succ
            f.succ = self.Node(x)

    def remove_all(self, x):
        """ Removes all ocurrencies of x in the list """
        self.first = self._remove_all(x, self.first)

    # def _remove_all(self, x, f):
    #     """ Task A5:
    #         Remove all x from list starting with node f.
    #         Return the first node in the remaing list.
    #     """
    #     if f == None:
    #         return None
    #
    #     if f.data == x:
    #         return self._remove_all(x, f.succ)
    #
    #     elif f.succ.data == x:
    #         f.succ = f.succ.succ
    #         return self._remove_all(x, f.succ)
    #     else:
    #         self._remove_all(x, f.succ)
    #         return f

    def remove_all(self, x):
        self.first = self._remove_all(x, self.first)

    def _remove_all(self, x, f):
        if f == None:
            return None
        elif x == f.data:
            return self._remove_all(x, f.succ)
        else:
            f.succ = self._remove_all(x, f.succ)
            return f

    def insert(self, data, index=0):
        """ B2: Inserts a new node at a specified index """
        pass


####################################


class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def __iter__(self):
            if self.left:
                yield from self.left
            yield self.data
            if self.right:
                yield from self.right

        def __str__(self):
            return str(self.data)

    def __init__(self, init=None):
        self.root = None
        if init:
            for x in init:
                self.add(x)

    def __iter__(self):
        if self.root:
            yield from self.root

    def __str__(self):
        result = ''
        for x in self:
            result += str(x) + ' '
        return '<' + result + '>'

    # def __eq__(self, other):
    #     for d in self:
    #         if other.contains(d) == False:
    #             return False
    #
    #     if self.size() == other.size():
    #         return True
    #     else:
    #         return False
    #
    # def size(self):
    #     return self._size(self.root)
    #
    # def _size(self, r):
    #     if r is None:
    #         return 0
    #     else:
    #         return 1 + self._size(r.left) + self._size(r.right)
    #
    #
    # def contains(self, k):               # Not compulsory
    #     return self._contains(self.root, k)
    # def _contains(self, f, k):
    #     if f is None:
    #         return False
    #     elif f.data == k:
    #         return True
    #     elif k < f.data:
    #         return self._contains(f.left,k)
    #     elif k > f.data:
    #         return self._contains(f.right,k)



    def __eq__(self, t):
        """ A8: Overloading =="""
        return str(self) == str(t)



    def add(self, x):
        """ Adds a new node to the tree"""
        def _add(x, r):
            if r == None:
                return self.Node(x)
            elif x < r.data:
                r.left = _add(x, r.left)
            elif x > r.data:
                r.right = _add(x, r.right)
            return r
        self.root = _add(x, self.root)

    def count_leaves(self):
        """ Returns the number of leaves """
        return self._count_leaves(self.root)

    def _count_leaves(self, r):
        """ A7:
            Count the leaves in the subtree with root r
        """
        if r is None:
            return 0

        elif r.left is None and r.right is None:
            return 1

        else:
            return self._count_leaves(r.left) + self._count_leaves(r.right)

    # def _count_leaves(self, r):
    #     """ A7:
    #         Count the leaves in the subtree with root r
    #     """
    #     if not r:
    #         return 0
    #     else:
    #         if r.left or r.right:
    #             return self._count_leaves(r.left) + self._count_leaves(r.right)
    #         else:
    #             return 1



def bst_sort(aList):
    """ Returns a sorted list"""
    bst = BST()
    for x in aList:
        bst.add(x)
    result = []
    for x in bst:
        result.append(x)
    return result




def main():
    # print('\nTest run of m3.py')
    #
    # print('\nTest of A5 (remove_all)')
    # lst = LinkedList()
    # for x in (3, 1, 2, 3, 4, 3, 4, 7, 3):
    #     lst.add_last(x)
    # print(lst)
    #
    # lst.remove_all(3)
    # print(lst, ' \t Should be (1, 2, 4, 4, 7)')

    # print('\nTest of B2 (insertion at an index)')
    # lst = LinkedList()
    # lst.insert(3)          # <3>
    # lst.insert(5, 1)       # <3, 5>
    # lst.insert(5)          # <5, 3, 5>
    # lst.insert(4, 1)       # <5, 4, 3, 5>
    # print(lst, ' \t Should be (5, 4, 3, 5)')
    # try:
    #     lst.insert(1, 99)      # LinkedListError: Index out range: 99
    # except ExamException as e:
    #     print(e)
    #
    # print('\nTest of A7: Number of leaves')
    # bst = BST([5, 2, 1, 3, 6, 4])
    # print('Number of leaves:', bst.count_leaves(), ' \t Should be 3')
    #
    # print("\nTest of A8: == for BST")
    print(BST() == BST(), ' \t Should be True')
    print(BST([1, 2, 3]) == BST([1, 2, 3]), ' \t Should be True')
    print(BST([2, 1, 3]) == BST([1, 2, 3]), ' \t Should be True')
    print(BST([0, 1, 3]) == BST([1, 2, 3]), ' \t Should be False')
    print(BST([1, 2, 3]) == BST([1, 2]), ' \t Should be False')
    #
    # print('\nDemonstration of bst_sort')
    # print(bst_sort([5, 2, 4, 8, 1, 9, 3]))


if __name__ == '__main__':
    main()

"""\n\nAnswer to task A6 - Complexity of repeated add_last:
    theta(n^2) d?? 
    
    The code starts with an empty list and the list grows for each add_last. The time for
code is then c*(0 + 1 + 2 + ... + n-1) = c*(n-1)*n which is Theta(n^2)

    """

"""\n\nAnswer to task B3 - Complexity of bst_sort:



    """
