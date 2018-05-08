#
# This file contains the Python code from Program 7.11 of
# "Data Structures and Algorithms
# with Object-Oriented Design Patterns in Python"
# by Bruno R. Preiss.
#
# Copyright (c) 2003 by Bruno R. Preiss, P.Eng.  All rights reserved.
#
# http://www.brpreiss.com/books/opus7/programs/pgm07_11.txt
#
class OrderedListAsLinkedList(OrderedList):

    def __init__(self):
        super(OrderedListAsLinkedList, self).__init__()
        self._linkedList = LinkedList()

    # ...
