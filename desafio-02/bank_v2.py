def welcome():
  welcome = """
  ----- 🏦 Welcome to Dio Bank -----
  """

  print(welcome)


def user_input():
  menu = """
  What do you want to do?
  [1] 💰 Cash Deposit
  [2] 💹 Bank Statement
  [3] 💸 Withdraw
  [0] ❌ Quit

  => """

  user_choice = input(menu)
  
  return user_choice


welcome()

def main():
  balance = 0
  LIMIT = 500
  statement = 0
  transactions_number = 0
  TRANSACTIONS_LIMIT = 3
  BANK_AGENCY = "0001"

  quit = False

  while not quit:
    choice = user_input()
    
    if choice == "0":
      quit = True

#   elif user_input == "1":
#     deposit = float(input("Enter amount to deposit: R$"))

#     if deposit > 0:
#       balance += deposit
#       statement = balance
#       print(
#           f"Deposit amount: R${deposit:.2f}\nYour new balance is: R${statement:.2f}\nDeposit Successful!"
#       )
#     else:
#       print("❗❗❗ERROR! Invalid deposit amount.")

#   elif user_input == "2":
#     print("---- Dio Bank Statement ----")
#     print("No bank transactions." if statement ==
#           0 else f"Your current balance is: R${statement:.2f}")

#   elif user_input == "3":
#     withdraw = float(input("Enter amount to withdraw: R$"))

#     if withdraw > 0:
#       if transactions_number < TRANSACTIONS_LIMIT:
#         if withdraw <= LIMIT:
#           if withdraw <= balance:
#             balance -= withdraw
#             transactions_number += 1
#             statement = balance
#             print(f"Succefully! Withdrawn amount: R${withdraw:.2f}")
#           else:
#             print("❗❗❗ERROR! Insufficient funds.")
#         else:
#           print("❗❗❗ERROR! Withdraw amount exceeds limit.")
#       else:
#         print("❗❗❗ERROR! Maximum number of transactions reached.")
#     else:
#       print("❗❗❗ERROR! Invalid withdraw amount.")

#   else:
#     print("❗❗❗ERROR! Invalid option.\nPlease choose a valid option...")

main()
