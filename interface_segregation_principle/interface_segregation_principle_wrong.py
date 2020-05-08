# Interface segregation principle:
#   A client should not have to implement an interface that it does not use.
#   Simply speaking, interfaces should be broken down.

# The code below violates the principle. The Human and Robot classes both inherit from Worker however
# the Robot class doesn't need to use the sleep method but is forced to implement it.

import abc


class Worker(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def work(self):
        return

    @abc.abstractmethod
    def sleep(self):
        return


class Human(Worker):
    def work(self):
        pass

    def sleep(self):
        pass


class Robot(Worker):
    def work(self):
        pass

    def sleep(self):
        pass


