# Build a class that includes a factory
class Factory:
    def __init__(self, brand):
        self.brand = brand

    def print(self):
        print("Brand:", self.brand)

    def extention(self, attribute):
        class Extend:
            def __init__(self, brand, extra):
                self.brand = brand
                setattr(self, attribute, extra)

            def print(self):
                print("Brand:", self.brand, f"{attribute}:", getattr(self, attribute))

        return Extend


# Create an object from the class
factory = Factory("Nike")

# Print the object attributes
factory.print()

# Utilize the factory to create a new class
Shoe = factory.extention("Size")

# Create an object from the new class
shoe = Shoe("Puma", "Large")

# Print the object attributes
shoe.print()








