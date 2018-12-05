#
# This file contains the Python code from Program A.3 of
# "Data Structures and Algorithms
# with Object-Oriented Design Patterns in Python"
# by Bruno R. Preiss.
#
# Copyright (c) 2003 by Bruno R. Preiss, P.Eng.  All rights reserved.
#
# http://www.brpreiss.com/books/opus7/programs/pgm0A_03.txt
#


class Complex(object):
    def get_real(self):
        return self._real

    def set_real(self, value):
        self._real = value

    real = property(
        fget=get_real,
        fset=set_real)

    def get_imag(self):
        return self._imag

    def set_imag(self, value):
        self._imag = value

    imag = property(
        fget=get_imag,
        fset=set_imag)

    # ...
