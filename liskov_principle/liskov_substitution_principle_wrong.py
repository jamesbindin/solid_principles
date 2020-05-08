# Liskov substitution principle:
#   A class can be replaced by its subclass in all practical scenarios.
# The program below violates the principle. the ostrich class is a bird, so it inherits from the bird class.
# However it shouldn't be using the fly method because ostriches can't fly

class Bird:
    def fly(self):
        print("Flying!!!")


class Duck(Bird):
    pass


class Ostrich(Bird):
    pass


obj = Ostrich()
obj.fly()#prints: Flying!!!



