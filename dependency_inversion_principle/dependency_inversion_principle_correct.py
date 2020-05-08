# Below the program has been edited according to the principle. The low level details have been abstracted out into
# abstract classes.


import abc


class Write(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(self):
        pass


class Send(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send(self):
        pass


class HighLevel(Write, Send):
    def write(self):
        print("writing high level")

    def send(self):
        print("sending high level")


class LowLevel(Write, Send):
    def write(self):
        print("writing low level")

    def send(self):
        print("sending low level")

