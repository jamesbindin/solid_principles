# single responsibility principle:
#   a class has a single responsibility
#   a class has one reason to change

# This program violates the single responsibility principle because the ComputeSaveEmail has three responsibilities.
class ComputeSaveEmail:
    def compute(self):
        print("computing data")

    def save(self):
        print("Saving Data")

    def email(self):
        print("Sending Email")


class CompleteTask:
    def __init__(self):
        self.compute_save_email = ComputeSaveEmail()

    def complete(self):
        self.compute_save_email.compute()
        self.compute_save_email.save()
        self.compute_save_email.email()

c = CompleteTask()
c.complete()



