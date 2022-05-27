""" linked_list.py

Student:Nils Wikström   
Mail: nils.wikstrom@outlook.com
Reviewed by: Sergi Olives Juan
Date reviewed: 2022-05-12
"""

from operator import index
from re import X
from xml.etree.ElementTree import tostring


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
        length = 0
        f = self.first
        while f:
            length = length +1
            f = f.succ
        return length
  
  
    def mean(self):               # Optional
        summa = 0
        length = 0
        f = self.first
        while f:
            length = length + 1
            summa = summa + f.data
            f = f.succ
        return(summa/length)
    
    def remove_last(self):        # Optional
        f = self.first
        if not f:
            return None
        while f:
            if not f.succ:
                data = self.first.data
                self.first = None
                return data
            if f.succ.succ == None:
                data = f.succ.data
                f.succ = None
                return data
            f = f.succ

    def remove(self, x):          # Compulsory
        f = self.first
        if f.data == x:
            f.data = f.succ.data
            f.succ = f.succ.succ
            return True
        while f:
            if f.succ == None:
                return False
            if f.succ.data != x:
                f = f.succ
            else:
                f.succ = f.succ.succ
                return True
    
    def count(self, x):           # Optional
        return self._count(x, self.first)

    def _count(self, x, f):
        if f is None:
            return 0
        elif f.data == x:
            return 1 + self._count(x,f.succ)
        else:
            return self._count(x,f.succ)
    
    
    def to_list(self):            # Compulsory
        lst = []
        f = self.first
        return self._to_list(f,lst)

    def _to_list(self,f,lst):
        if f is None:
            return lst
        else:
            lst.append(f.data)
            return self._to_list(f.succ,lst)
        
    
    def remove_all(self, x):      # Compulsory
        f = self.first
        return self._remove_all(x,f)

    def _remove_all(self,x,f):
        if not f.succ and f.data == x:
            self.remove_last()
            return None
        if f.data == x and f:
            f.data = f.succ.data
            f.succ = f.succ.succ
            return self._remove_all(x,f)
        if f.succ:
            return self._remove_all(x, f.succ)
    
    def __str__(self):            # Compulsary
        ret = '('
        len = self.length()
        n = 0
        for i in self.__iter__():
            if n == len-1:
                ret = ret + str(i)
            else:
                ret = ret + str(i) + ', '
            n = n +1
        return ret + ')'
    
    
    def merge(self, lst):           # Compulsory
        for i in lst:               
            self.insert(i)
        return self                 #Complexity worst case: n^2 , best case n + 1
        
    def __getitem__(self, ind):   # Compulsory
        indx = 0
        f = self.first
        while f:
            if ind == indx:
                return f.data
            indx = indx + 1
            f = f.succ


class Person:                     # Compulsory to complete
    def __init__(self,name, pnr):
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return f"{self.name}:{self.pnr}"

    def __lt__(self,other):
        if self.pnr < other.pnr:
            return True
        else:
            return False
    
    def __le__(self,other):
        if self.pnr <= other.pnr:
            return True
        else:
            return False
    
    def __gt__(self,other):
        if self.pnr > other.pnr:
            return True
        else:
            return False
    
    def __ge__(self,other):
        if self.pnr >= other.pnr:
            return True
        else:
            return False
    
    def __eq__(self,other):
        if self.pnr == other.pnr:
            return True
        else:
            return False
    
    def __ne__(self,other):
        if self.pnr != other.pnr:
            return True
        else:
            return False

    

def main():
    lst = LinkedList()
    per1 = Person('Klas', 19996969)
    per2 = Person('Lukas', 20004202)
    per3 = Person('Mamma', 19986969)
    per4 = Person('Gustav', 20000825)

    templst = [per1,per2,per3,per4]
    for x in templst:
        lst.insert(x)
    lst.print()


if __name__ == '__main__':
    main()
    


    

