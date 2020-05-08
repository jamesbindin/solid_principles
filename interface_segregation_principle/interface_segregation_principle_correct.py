# Below the program has been changed according to the principle. The work and sleep methods have been separated into
# two abstract classes allowing Human and Robot classes implement the separate behaviours as needed. This adds more
# extendability to our program.
import abc


class Worker(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def work(self):
        return


class Sleeper(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sleep(self):
        return


class Human(Worker, Sleeper):
    def work(self):
        pass

    def sleep(self):
        pass


class Robot(Worker):
    def work(self):
        pass

