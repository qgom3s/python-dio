def welcome():
    welcome_message = """
    ----- 🏦 Welcome to Dio Bank -----
    """
    print(welcome_message)


def customer_menu():
    menu = """
    What do you want to do?
    [1] 💰 Cash Deposit
    [2] 💹 Bank Statement
    [3] 💸 Withdraw
    [0] ❌ Quit

    => """
    
    return menu


def user_input():
    user_choice = input(customer_menu())
    
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


def operations():
    balance = 0
    transactions_number = 0
    bank_statement = []
    LIMIT = 500
    TRANSACTIONS_LIMIT = 3
    
    quit = False
    
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

    
def create_customer(customers):
    name = input("Enter user name: ")
    cpf = input("Enter user CPF: ")

    if any(customer['cpf'] == cpf for customer in customers):
        print("❗❗❗ERROR! CPF already registered.")
        return customers

    new_customer = {'name': name, 'cpf': cpf}
    customers.append(new_customer)
    print(f"✔️User {name} added successfully.")
    return customers


def create_account(customers, accounts, branch):
    cpf = input("Enter user CPF to create a new account: ")

    user_found = next((customer for customer in customers if customer['cpf'] == cpf), None)

    if not user_found:
        print("❗❗❗ERROR! User not found.")
        return accounts

    new_account = {'account_number': len(accounts) + 1, 'agencia': branch, 'user': user_found}
    accounts.append(new_account)
    print(f"✔️Account created successfully. Account number: {new_account['account_number']}")
    return accounts


def list_customers(customers):
    print("---- 🙎🏻‍♂️ List of Users ----")
    for user in customers:
        print(f"Name: {user['name']}, CPF: {user['cpf']}")
    print("----------------------------")


def list_accounts(accounts):
    print("---- 🗂️ List of Accounts ----")
    for account in accounts:
        user_name = account['user']['name']
        account_number = account['account_number']
        print(f"Account Number: {account_number}, User: {user_name}")
    print("----------------------------")


def adm_menu():
    menu = """
    What do you want to do?
    [1] 🛎️ Add new customer
    [2] 📑 Add new account
    [3] 📝 List of customers
    [4] 📜 List of accounts
    [0] ❌ Quit

    => """
    
    return menu


def user_management():
    BRANCH_BANK = "0001"
    customers = [{'name': 'John Smit', 'cpf': '00120045607'},]
    accounts = [{'account_number': 1, 'agencia': '0001', 'user': {'name': 'John Smith', 'cpf': '00120045607'}},]
    
    while True:
        adm_choice = input(adm_menu())
        
        if adm_choice == "1":
            customers = create_customer(customers)
        elif adm_choice == "2":
            accounts = create_account(customers, accounts, BRANCH_BANK)
        elif adm_choice == "3":
            list_customers(customers)
        elif adm_choice == "4":
            list_accounts(accounts)
        elif adm_choice == "0":
            break
        else:
            print("❗❗❗ERROR! Invalid option.\nPlease choose a valid option...")
        
        
def main():
    
    welcome()
    
    into = """
    What do you want to do?
    [1] ❓ Test User features
    [2] ❔ Test Manager features
    => """
    
    lets_go = input(into)
    
    if lets_go == '1':
        operations()
    elif lets_go == '2':
        user_management()
    else:
        print("❗❗❗ERROR! Invalid option.")
    
    
main()
