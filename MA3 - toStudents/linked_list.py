""" linked_list.py

Student: David Lood
Mail: david.lood.3070@student.uu.se
Reviewed by: Xiaoxia Liu
Date reviewed: 28/9
"""

class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None


    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')


    # To be implemented

    def length(self):             # Optional
        count = 0
        f = self.first
        if f is not None and f.data is None:
            return count
        while f:
            count += 1
            f = f.succ
        return count



    def mean(self):               # Optional
        f = self.first
        if f == None:
            return None
        sum = 0
        while f:
            sum += f.data
            f = f.succ
        return sum / self.length()



    def remove_last(self):        # Optional
        f = self.first
        if f == None:
             return
        elif f.succ == None:
            result = f.data
            f.data = f.succ
            return result

        while f:
            if f.succ.succ == None:
                result = f.succ.data
                f.succ = f.succ.succ
            f = f.succ
        return result



    def remove(self, x):          # Compulsory
        f = self.first
        if f == None:
            return False
        elif f.data == x:
            self.first = f.succ
            return True

        while f:
            if f.succ == None:
                return False
            elif f.succ.data == x:
                f.succ = f.succ.succ
                return True
            f = f.succ



    def count(self,x):           # Optional
        return self._count(self.first, x)

    def _count(self,f, x):
        if f is None:
            return 0
        elif f.data == x:
            return 1 + self._count(f.succ,x)
        else:
            return self._count(f.succ,x)





    def to_list(self):            # Compulsory
        lista = []
        self._to_list(self.first, lista)
        return lista

    def _to_list(self, f, lista):
        if f is None:
            return
        else:
            lista.append(f.data)
            self._to_list(f.succ,lista)




    def remove_all(self, x):      # Compulsory
        if self.remove(x) == True:
            return self.remove_all(x)
        else:
            return




    def get_last(self):
        f = self.first
        while f:
            if f.succ == None:
                return f.data
            f = f.succ


    def __str__(self):            # Compulsary
        result=('(')
        for d in self:
            if d == self.get_last():
                result += str(d)
                break
            else:
                result += str(d)+', '
        return result +')'




    def copy(self):               # Compulsary
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result


    # ''' Complexity for this implementation:
    # Theta(n^2) metod
    # '''


    def copy(self):               # Compulsary
        result = LinkedList()
        f = self.first
        result.first = f

        if f is None:
            return result

        while f.succ:
            result.Node(f.data, f.succ)
            f = f.succ
        return result

    # ''' Complexity for this implementation:
    # Theta(n) method
    #  '''


    def __getitem__(self, ind):   # Compulsory
        count = 0
        f = self.first
        if f is None:
            print('index out of range')
            return ''
        while f:
            if count == ind:
                return f.data
                break
            elif f.succ == None:
                print('index out of range')
                return ''
                break
            count += 1
            f = f.succ


class Person:                     # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"

    #Antingen nr:

    def __lt__(self,other):
        return self.pnr < other.pnr

    def __le__(self, other):
        return self.pnr <= other.pnr

    def __gt__(self,other):
        return self.pnr > other.pnr

    def __ge__(self,other):
        return self.pnr >= other.pnr

    def __eq__(self, other):
        return self.pnr == other.pnr

    def __ne__(self, other):
        return self.pnr != other.pnr


    # Elr namn:

    # def __lt__(self,other):
    #     return self.name < other.name
    #
    # def __le__(self, other):
    #     return self.name <= other.name
    #
    # def __gt__(self,other):
    #     return self.name > other.name
    #
    # def __ge__(self,other):
    #     return self.name <= other.name
    #
    # def __eq__(self, other):
    #     return self.name == other.name
    # def __ne__(self, other):
    #     return self.name != other.name




def main():
    lst = LinkedList()
    for x in []:
        lst.insert(x)
    print(lst)


    # # Test code:
    # print(lst.length())
    # print(lst.mean())
    # print(lst.remove_last())
    # print(lst.lst.remove(1))
    # print(lst.count(1))
    # lst = lst.to_list()
    # print(lst.__str__())
    # print(lst.get_last())
    # lst.print()
    # hej = lst.copy()
    # hej.print()
    # print(hej.length())
    # print(lst[3])

    # namn = LinkedList()
    # David = Person('David', 5)
    # Karl = Person('Karl', 3)
    # Lisa = Person('Lisa', 10)
    # Adam = Person('Adam',1)
    # namn.insert(David)
    # namn.insert(Karl)
    # namn.insert(Lisa)
    # namn.insert(Adam)
    # print(namn)

    # lst = LinkedList()
    # print(lst)
    # lst.insert(2)
    # print(lst)
    # lst.insert(1)
    # print(lst)
    #
    # for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
    #     lst.insert(x)
    # print(lst)
    # print('length(): ', lst.length())
    # print('mean()  : ', lst.mean())
    #
    #
    # for x in [0, 1, 2, 9, 10]:
    #     print(f"{lst} remove({x}): {lst.remove(x)}, {lst}")
    #
    # for x in lst:
    #     print(x, end=' ')
    # print()
    #
    # print('str:', lst)
    #
    # lst = LinkedList()
    # for x in (3, 1, 8, 2, 8, 5, 1, 4):
    #     lst.insert(x)
    # print('lst      :', lst)
    # print('copy(lst):', lst.copy())


if __name__ == "__main__":
    main()