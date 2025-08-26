# Create another class that your initial class relies on for one of the attributes
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def bond(self):
        z = ""

        if self.x + self.y == "ab":
            z = "c"
        else:
            z = self.x + self.y
        return z

# Create a class of your choice with at least 3 attributes and 1 method
class B:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print(self):
        print("a:", self.a)
        print("b:", self.b)
        print("c:", self.c.bond())

#Create an object from your class
m = A("a", "b")

# Use dependency injection to create another object
n = B("a", "b", m).print()