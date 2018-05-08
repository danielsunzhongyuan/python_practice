#
# This file contains the Python code from Program 7.20 of
# "Data Structures and Algorithms
# with Object-Oriented Design Patterns in Python"
# by Bruno R. Preiss.
#
# Copyright (c) 2003 by Bruno R. Preiss, P.Eng.  All rights reserved.
#
# http://www.brpreiss.com/books/opus7/programs/pgm07_20.txt
#
class Polynomial(Container):

    def __init__(self):
        super(Polynomial, self).__init__()

    def addTerm(self, term):
        pass
    addTerm = abstractmethod(addTerm)

    def differentiate(self):
        pass
    differentiate = abstractmethod(differentiate)

    def __add__(self, polynomial):
        pass
    __add__ = abstractmethod(__add__)

    # ...
