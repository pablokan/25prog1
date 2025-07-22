class A:
    def __init__(self):
        self.value = 1

    def method(self):
        return self.value
    
a = A()
b = a.method()
print(b)  # Output: 1
