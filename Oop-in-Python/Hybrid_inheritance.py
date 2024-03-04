class A:
    '''This is normal Class
    And that class Have not attribute.'''
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

a = A()


# MRO Method

print(D.__mro__)
print(A.__doc__)
help(a)



