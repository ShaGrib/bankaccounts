class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = BankAccount()
    def make_deposit(self, amount):
        print(f"{self.name} hands ${amount} to the teller")
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        print(f"{self.name} asks the teller for ${amount} from the account")
        self.account.withdraw(amount)
        return self
    def ask_interest_approval(self):
        print(f"{self.name} asks teller to approve interest")
        self.account.yield_interest()
        return self
    def display_user_balance(self):
        print(f"{self.name} asks the teller to show the balance of the account")
        self.account.display_account_info()
        return self

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds;
# if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate
# (as long as the balance is positive)

class BankAccount:
    def __init__(self, int_rate = .02, balance= 0): 
        self.interest = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance <= 0:
            print(f"Insufficient funds: Charging a $5 Fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def yield_interest(self):
        if self.balance >= 1:
            self.balance += self.balance * self.interest
            print(f"Teller responds, telling you they can approve interest on your savings")
        else:
            print(f"Teller responds, telling you there is not enough funds in the account to approve the interest accrual")
        return self
    def display_account_info(self):
        print(f"Balance: ${(float(round(self.balance, 2)))}")
        return self
    # def display_all_accounts(User):
    #     print(f"Accounts {User.account}")

guido = User("Guido der Rothchild", "guido@python.com", "4413223")
monty = User("Monty Python", "monty@python.com", "4413224")
armen = User("Armen van Tollen", "armen@moomoomail.com", "4413225")
guido.bank_name = "Dojo Credit Union"
# bank = BankAccount()

guido.display_user_balance()
monty.display_user_balance()
armen.display_user_balance()

guido.make_deposit(950).make_deposit(674).make_deposit(783).make_withdrawal(305).ask_interest_approval().display_user_balance()
# monty.make_deposit(1000).make_deposit(2500).ask_interest_approval()
# monty.display_user_balance()
# armen.make_deposit(100).make_withdrawal(87).make_withdrawal(64).make_withdrawal(10).ask_interest_approval()
# armen.display_user_balance()