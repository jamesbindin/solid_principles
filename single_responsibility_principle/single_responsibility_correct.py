# The ComputeSaveEmail class has now been broken down into three classes, each with their own
# responsibility. This program no longer violates the single responsibility principle.


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



