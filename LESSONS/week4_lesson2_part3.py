class Class:
    pass

obj = Class()

print(type(obj))
print(type(Class))

def dummy_factory():
    class Class1:
        pass
    return Class1

Dummy = dummy_factory()

print(Dummy() is Dummy())