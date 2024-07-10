class A:
    def __init__(self):
        self.var_a="variable a"
    def method_a(self):
        return "this is method from a"
    
class B(A):
    def __init__(self):
        super().__init__()
        self.var_b="variable b"
    def method_b(self):
            return "this is mehod from b"

class C(B):
    def __init__(self):
          super().__init__()
          self.var_c="variable c"
    def method_c(self):
         return "this is method from c"
obj_c=C()

print(obj_c.var_a)
print(obj_c.method_a())
print(obj_c.var_c)