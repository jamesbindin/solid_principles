# Dependency inversion principle:
#   High-level modules should not depend on low-level modules. Both should depend on abstractions.
#   Abstractions should not depend upon details. Details should depend upon abstractions.
# simply put higher level modules should not extend lower level modules. if needed the behaviours should be abstracted
# using abstract classes or interfaces.

# The code below violates the principle. A higher level module is composed of a lower level module.

class HighLevel:
    def __init__(self):
        self.lower_level = LowLevel()

    def call(self):
        self.lower_level.write()
        self.lower_level.send()


class LowLevel:
    def write(self):
        print("writing")

    def send(self):
        print("sending")

high = HighLevel()
high.call()# prints: "writing"
           #         "sending"
