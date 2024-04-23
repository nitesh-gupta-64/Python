class O:
    def fun(self):
        print("Class O")
        super().fun()

class X(O):
    def fun(self):
        print("Class X")
        super().fun()

class Y(O):
    def fun(self):
        print("Class Y")
        super().fun()

class Z(O):
    def fun(self):
        print("Class Z")
        super().fun()

class A(X, Y):
    def fun(self):
        print("Class A")
        super().fun()

class B(Y, Z):
    def fun(self):
        print("Class B")
        super().fun()

class M(A, B, Z):
    def fun(self):
        print("Class M")
        super().fun()

m = M()
m.fun()
