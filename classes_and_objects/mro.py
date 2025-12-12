class A:
    label = "A: Chai Blend"

class B(A):
    label = "B: Masala Blend"

class C(A):
    label = "C: Lemon Blend"

class D(B, C):
    pass

cup  = D()
print(cup.label)