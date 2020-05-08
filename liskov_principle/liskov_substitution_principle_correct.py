
class Bird:
    def get_info(self):
        print("I am a Bird")


class FlyingBird(Bird):
    def fly(self):
        print("Flying!!!")


class Duck(FlyingBird):
    pass


class Ostrich(Bird):
    pass


obj = Ostrich()
#obj.fly()# gives error
obj.get_info()# prints: "I am a Bird"



