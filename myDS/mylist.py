#!/usr/bin/env python
######################################################
# Name    : mylist.py
# Date    : 02-October-2017
######################################################

class MyNode(object):
    def __init__(self):
        """Constructor for Node
        :returns: TODO

        """
        self.data = val
        self._next = None

    @property
    def data(self):
        """Getter for data
        :returns: TODO

        """
        return self._data

    @property
    def next(self):
        """Getter for next
        :returns: TODO

        """
        return self._next

    @property.setter
    def data(self, val):
        """Setter for data

        :val: TODO

        """
        self._data = val

    @property.setter
    def next(self, val):
        """Setter for next.

        :val: TODO

        """
        self._next = val


class MyList(MyNode):

    """Docstring for MyList. """

    def __init__(self):
        """TODO: to be defined1. """
        self.head = None
    
    def isEmpty(self):
        """TODO: Docstring for isEmpty.
        :returns: TODO

        """
        return True if self.head is None else False 

    def add(self, val):
        """TODO: Docstring for add.
        :returns: TODO

        """
        tmpnode = MyNode(val)
        tmpnode.next = self.head 
        self.head = tmpnode

    def size(self):
        """TODO: Docstring for size.
        :returns: TODO

        """
        curr = self.head 
        count = 0
        while curr is not None:
            count = count + 1
            curr = curr.next
        return count

    def search(self, val):
        """TODO: Docstring for search.
        :returns: TODO

        """
        curr = self.head 
        while curr != None:
            if curr.data == val:
                return True
            curr = curr.next 
        return False
