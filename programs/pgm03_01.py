#
# This file contains the Python code from Program 3.1 of
# "Data Structures and Algorithms
# with Object-Oriented Design Patterns in Python"
# by Bruno R. Preiss.
#
# Copyright (c) 2003 by Bruno R. Preiss, P.Eng.  All rights reserved.
#
# http://www.brpreiss.com/books/opus7/programs/pgm03_01.txt
#
def Horner(a, n, x):
    result = a[n]
    i = n - 1
    while i >= 0:
        result = result * x + a[i]
        i -= 1
    return result
    # a0 + a1 * x + a2 * x^2 + a3 * x^3 + ... + an * x^n
    # Horner([1,1,1,1], 3, 2) ==> 15