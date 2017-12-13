#a)
a = [3,6,8,9]

#b)
b = a

#c)
b[1] = 20
#d) list a is also changed in the same way, since we're using pointers, any changes to b will point to the address of a and change that.

#e)
c = a[:]


#f)
c[2] = 30

#g) list a is unchanged even though we changed c. The change to c is likely a copy now, so the original list of a is unchanged.


def set_first_elem_to_zero(l):
    l[0] = 0
    return l

# The original list is modified - the first element is 0 now.
