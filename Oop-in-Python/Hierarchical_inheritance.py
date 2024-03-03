class A:
    a = 10
    pass

class B(A):
    b = 10
    pass
class C(A):
    pass

c1 = C()
print(c1.a) 