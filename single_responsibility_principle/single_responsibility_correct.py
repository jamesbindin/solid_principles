# The ComputeSaveEmail class has now been broken down into three classes, each with their own
# responsibility. This program no longer violates the single responsibility principle.
# this ensures each class can be reused and extended without unwanted behaviours coupled to the classes.
# following the single responsibility principle also makes code more readable.
class Compute:
    def compute(self):
        print("computing data")


class Save:
    def save(self):
        print("Saving Data")


class Email:
    def email(self):
        print("Sending Email")


class CompleteTask:
    def __init__(self):
        self.compute = Compute()
        self.save = Save()
        self.email = Email()

    def complete(self):
        self.compute.compute()
        self.save.save()
        self.email.email()


c = CompleteTask()
c.complete()



