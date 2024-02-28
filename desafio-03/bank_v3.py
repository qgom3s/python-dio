from datetime import datetime

class WelcomeMessage:
    @staticmethod
    def display():
        welcome_message = """
        ----- 🏦 Welcome to Dio Bank -----
        """
        print(welcome_message)


class CustomerMenu:
    @staticmethod
    def menu():
        menu = """
        What do you want to do?
        [1] 💰 Cash Deposit
        [2] 💹 Bank Statement
        [3] 💸 Withdraw
        [0] ❌ Quit

        => """
        
        return menu


class UserInput:
    @staticmethod
    def user_input():
        user_choice = input(CustomerMenu.menu())
        
        return user_choice


class Transaction:
    @staticmethod
    def register_transaction(account, transaction_type, value):
        account.history.add_transaction(transaction_type(value))


class Operations:
    @staticmethod
    def perform_operations(account):
        balance = account.balance
        transactions_number = 0
        bank_statement = account.history.transactions
        LIMIT = 500
        TRANSACTIONS_LIMIT = 3
        
        quit = False
        
        while not quit:
            choice = UserInput.user_input()
            
            if choice == "0":
                quit = True
            elif choice == "1":
                deposit_amount = float(input("Enter amount to deposit: $"))
                balance, bank_statement = account.deposit(deposit_amount, bank_statement)
            elif choice == "2":
                account.get_statement()
            elif choice == "3":
                withdraw_amount = float(input("Enter amount to withdraw: $"))
                balance, bank_statement, transactions_number = account.withdraw(
                    withdraw_amount, bank_statement, balance, LIMIT, TRANSACTIONS_LIMIT, transactions_number
                )
            else:
                print("❗❗❗ERROR! Invalid option.\nPlease choose a valid option...")

class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def perform_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)

class Person(Client):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf


class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    def withdraw(self, value, statement, balance, limit, withdrawals_limit, withdrawals_number):
        if value > 0:
            if withdrawals_number < withdrawals_limit:
                if value <= limit:
                    if value <= balance:
                        balance -= value
                        withdrawals_number += 1
                        statement.append({"type": "Withdrawal", "value": -value, "date": datetime.now()})
                        print(f"✔️ Successfully! Withdrawn amount: ${value:.2f}")
                    else:
                        print("❗❗❗ERROR! Insufficient funds.")
                else:
                    print("❗❗❗ERROR! Withdraw amount exceeds limit.")
            else:
                print("❗❗❗ERROR! Maximum number of transactions reached.")
        else:
            print("❗❗❗ERROR! Invalid withdraw amount.")
        
        return balance, statement, withdrawals_number

    def deposit(self, value, statement):
        if value > 0:
            self._balance += value
            statement.append({"type": "Deposit", "value": value, "date": datetime.now()})
            print(f"✔️ Successfully! Deposited amount: ${value:.2f}")
        else:
            print("❗❗❗ERROR! Invalid deposit amount.")

        return self._balance, statement

    def get_statement(self):
        print("---- 🏦 Dio Bank Statement ----")
        if not self._history.transactions:
            print("⚠️ No bank transactions.")
        else:
            print(f"⏳ Your current balance is: ${self._balance:.2f}")
            print(f"📃 Deposit history:")
            for transaction in self._history.transactions:
                type_ = transaction["type"]
                value = transaction["value"]
                date = transaction["date"].strftime("%d-%m-%Y %H:%M:%S")
                if type_ == "Withdrawal":
                    print(f"➖ ${-value} at {date}")
                else:
                    print(f"➕ ${value} at {date}")


class History:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(transaction)


class CheckingAccount(Account):
    def __init__(self, number, client, limit=500, withdrawals_limit=3):
        super().__init__(number, client)
        self.limit = limit
        self.withdrawals_limit = withdrawals_limit

    def withdraw(self, value, statement, balance, limit, withdrawals_limit, withdrawals_number):
        withdrawals = len([transaction for transaction in statement if transaction["type"] == "Withdrawal"])

        if value > self.limit:
            print("\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@")

        elif withdrawals >= self.withdrawals_limit:
            print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

        else:
            return super().withdraw(value, statement, balance, limit, withdrawals_limit, withdrawals_number)

    def __str__(self):
        return f"""\
            Agency:\t{self.agency}
            Account:\t{self.number}
            Holder:\t{self.client.name}
        """


def main():
    WelcomeMessage.display()

    # Aqui você pode criar uma instância de PessoaFisica e ContaCorrente
    # e passá-las para a função perform_operations() para realizar as operações.
    # Por exemplo:
    client1 = Person(name="John Doe", birth_date=datetime(1990, 1, 1), cpf="12345678900", address="123 Main St")
    account1 = CheckingAccount(number=1, client=client1)
    Operations.perform_operations(account1)

    

main()
