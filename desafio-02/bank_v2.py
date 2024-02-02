def welcome():
    welcome_message = """
    ----- 🏦 Welcome to Dio Bank -----
    """
    print(welcome_message)


def menu():
    menu = """
    What do you want to do?
    [1] 💰 Cash Deposit
    [2] 💹 Bank Statement
    [3] 💸 Withdraw
    [0] ❌ Quit

    => """
    
    return menu


def user_input():
    user_choice = input(menu())
    
    return user_choice


def deposit(balance, amount, bank_statement):
    if amount > 0:
        balance += amount
        bank_statement.append(amount)
        print(f"📥Deposit amount: R${amount:.2f}\n⏳Your new balance is: R${balance:.2f}\n✔️Deposit Successful!")
    else:
        print("❗❗❗ERROR! Invalid deposit amount.")
    
    return balance, bank_statement


def get_statement(balance, *, bank_statement):
    print("---- 🏦 Dio Bank Statement ----")
    if not bank_statement:
        print("⚠️No bank transactions.")
    else:
        print(f"⏳Your current balance is: R${balance:.2f}")
        print(f"📃Deposit history:")
        for deal in bank_statement:
            if deal < 0:
                print(f"➖${(deal * (-1))}")
            else:
                print(f"➕${deal}")


def withdraw(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > 0:
        if numero_saques < limite_saques:
            if valor <= limite:
                if valor <= saldo:
                    saldo -= valor
                    numero_saques += 1
                    extrato.append(-valor)
                    print(f"✔️Successfully! Withdrawn amount: R${valor:.2f}")
                else:
                    print("❗❗❗ERROR! Insufficient funds.")
            else:
                print("❗❗❗ERROR! Withdraw amount exceeds limit.")
        else:
            print("❗❗❗ERROR! Maximum number of transactions reached.")
    else:
        print("❗❗❗ERROR! Invalid withdraw amount.")
    
    return saldo, extrato, numero_saques


def main():
    balance = 0
    transactions_number = 0
    bank_statement = []
    LIMIT = 500
    TRANSACTIONS_LIMIT = 3
    BRANCH_BANK = "0001"
    
    quit = False
    
    welcome()
    
    while not quit:
        choice = user_input()
        
        if choice == "0":
            quit = True
        elif choice == "1":
            deposit_amount = float(input("Enter amount to deposit: R$"))
            balance, bank_statement = deposit(balance, deposit_amount, bank_statement)
        elif choice == "2":
            get_statement(balance, bank_statement=bank_statement)
        elif choice == "3":
            withdraw_amount = float(input("Enter amount to withdraw: $"))
            balance, bank_statement, transactions_number = withdraw(
                saldo=balance,
                valor=withdraw_amount,
                extrato=bank_statement,
                limite=LIMIT,
                numero_saques=transactions_number,
                limite_saques=TRANSACTIONS_LIMIT
            )
        else:
            print("❗❗❗ERROR! Invalid option.\nPlease choose a valid option...")

    
main()
