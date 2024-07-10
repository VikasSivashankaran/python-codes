class A:
    
    def method_a(self):
        return "Method a"
    
class B(A):
    
    def method_b(self):
            return "Method B"

class C(B):
    
    def method_c(self):
         return "method c"
c_instance=C()
print(c_instance.method_a())
print(c_instance.method_b())
print(c_instance.method_c())

