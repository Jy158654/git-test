import datetime
history = {}


class Account:
    def __init__(self):
        self.pin = 1234

    def checkCode(self,value):
        return self.pin == value

    def checkBalance(self):
        print("Current balance is {} euros".format(self.balance))

    def checkTransactions(self):
        print("Previous transactions:")
        for item in sorted(history):
            print("{} \t\t {} euros".format(item,history[item]))

    def withdraw(self,pin,value):
        if self.checkCode(pin):
            if value <= self.balance:
                current_time = datetime.datetime.now()
                history.update({current_time:-value})
                self.balance -= value
                print("Successfully withdrawn " + str(value) + " euros from your account.")
            else:
                print("Not enough balance")
        else:
            print("Wrong pin code.Try again.")

    def deposit(self,pin,value):
        if self.checkCode(pin):
            current_time = datetime.datetime.now()
            history.update({current_time:+value})
            self.balance += value
            print("Successfully deposited {} euros from your account.".format(value))
        else:
            print("Wrong pin code.Try again.")

    def createMBNet(self,value):
        import random
        self.MBalance = value
        print("You have successfully created an MBNet card with {} euros".format(value))
        card_ID = [random.randint(0,9) for i in range(4)]
        print("Your card ID is {}".format("".join(str(i) for i in card_ID)))
        card_secret = [random.randint(0,9) for i in range(4)]
        print("You secret code is {}".format("".join(str(i) for i in card_secret)))

    def changePIN(self,old_value,new_value):
        if self.checkCode(old_value):
            self.pin = new_value
            print("Pin code has been successfully changed to {}".format(new_value))
        else:
            print("Wrong pin code.Try again.")


class CheckingAccount(Account):
    def __init__(self):
        super().__init__()
        self.balance = 12000

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.balance = 5000

class BusineesAccount(Account):
    def __init__(self):
        super().__init__()
        self.balance = 10000

checkAcc = CheckingAccount()
print("Enter pin:")
pin = input()


class MessageWriter():
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self):
        self.file.close()

with MessageWriter('my_file.txt') as xfile:
    xfile.write('hello world')

