# Hybrid inheritance

class A:
    pass


class B(A):
    pass

class C(B):
    pass


class All(A,B,C):
    pass


# We create a new class using existing class or by combining class


# Hierachical Inheritance


class baseclass:
    pass


class D1(baseclass):
    pass

class D3(baseclass):
    pass

class D4(D3):
    pass

